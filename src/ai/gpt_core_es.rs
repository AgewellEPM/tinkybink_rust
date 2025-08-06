//! 🧠💥 Núcleo GPT-Infundido para Modelo Pequeño - ESPAÑOL
//! 
//! Dale inteligencia tipo GPT a CUALQUIER modelo pequeño a través de:
//! - Flujo de atención causal
//! - Predicción de tokens
//! - Ventanas de contexto
//! - Mapeo emocional

use anyhow::Result;
use std::collections::VecDeque;
use serde::{Serialize, Deserialize};

/// Configuración del modelo GPT español
#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct ConfiguracionGPT {
    pub tamaño_vocabulario: usize,
    pub dim_oculta: usize,
    pub num_capas: usize,
    pub num_cabezas: usize,
    pub longitud_contexto: usize,
    pub tasa_abandono: f32,
    pub temp_emocional: f32,
}

impl Default for ConfiguracionGPT {
    fn default() -> Self {
        Self {
            tamaño_vocabulario: 50000,
            dim_oculta: 768,
            num_capas: 12,
            num_cabezas: 12,
            longitud_contexto: 1024,
            tasa_abandono: 0.1,
            temp_emocional: 0.7,
        }
    }
}

/// Estado emocional con inteligencia española
#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct EstadoEmocional {
    pub valencia: f32,      // -1.0 (negativo) a 1.0 (positivo)
    pub activacion: f32,    // 0.0 (calmado) a 1.0 (excitado)
    pub dominancia: f32,    // 0.0 (sumiso) a 1.0 (dominante)
    pub expresividad: f32,  // 0.0 (reservado) a 1.0 (expresivo)
    pub pasion: f32,        // Característica española: pasión/intensidad
}

impl Default for EstadoEmocional {
    fn default() -> Self {
        Self {
            valencia: 0.5,
            activacion: 0.5,
            dominancia: 0.5,
            expresividad: 0.7,  // Los españoles son más expresivos
            pasion: 0.6,        // Mayor pasión por defecto
        }
    }
}

/// Motor de atención causal en español
pub struct MotorAtencion {
    pesos_q: Vec<Vec<f32>>,
    pesos_k: Vec<Vec<f32>>,
    pesos_v: Vec<Vec<f32>>,
    pesos_salida: Vec<Vec<f32>>,
    num_cabezas: usize,
    dim_cabeza: usize,
}

impl MotorAtencion {
    pub fn nuevo(dim_oculta: usize, num_cabezas: usize) -> Self {
        let dim_cabeza = dim_oculta / num_cabezas;
        
        Self {
            pesos_q: Self::inicializar_pesos(dim_oculta, dim_oculta),
            pesos_k: Self::inicializar_pesos(dim_oculta, dim_oculta),
            pesos_v: Self::inicializar_pesos(dim_oculta, dim_oculta),
            pesos_salida: Self::inicializar_pesos(dim_oculta, dim_oculta),
            num_cabezas,
            dim_cabeza,
        }
    }
    
    fn inicializar_pesos(filas: usize, cols: usize) -> Vec<Vec<f32>> {
        let escala = (2.0 / filas as f32).sqrt();
        (0..filas)
            .map(|_| {
                (0..cols)
                    .map(|_| rand::random::<f32>() * escala - escala / 2.0)
                    .collect()
            })
            .collect()
    }
    
    pub fn adelante(&self, x: &[Vec<f32>], mascara: Option<&[Vec<bool>]>) -> Vec<Vec<f32>> {
        let longitud_seq = x.len();
        let dim_oculta = x[0].len();
        
        // Proyectar a Q, K, V
        let q = self.proyectar(&x, &self.pesos_q);
        let k = self.proyectar(&x, &self.pesos_k);
        let v = self.proyectar(&x, &self.pesos_v);
        
        // Remodelar para cabezas múltiples
        let q_cabezas = self.remodelar_cabezas(&q);
        let k_cabezas = self.remodelar_cabezas(&k);
        let _v_cabezas = self.remodelar_cabezas(&v);
        
        // Calcular puntuaciones de atención
        let mut puntuaciones = vec![vec![0.0; longitud_seq]; longitud_seq];
        let escala = (self.dim_cabeza as f32).sqrt();
        
        for i in 0..longitud_seq {
            for j in 0..longitud_seq {
                // Atención causal: no atender a posiciones futuras
                if j > i {
                    puntuaciones[i][j] = -1e10;
                } else {
                    let mut puntuacion = 0.0;
                    for h in 0..self.num_cabezas {
                        for d in 0..self.dim_cabeza {
                            puntuacion += q_cabezas[h][i][d] * k_cabezas[h][j][d];
                        }
                    }
                    puntuaciones[i][j] = puntuacion / escala;
                }
            }
        }
        
        // Aplicar máscara si se proporciona
        if let Some(m) = mascara {
            for i in 0..longitud_seq {
                for j in 0..longitud_seq {
                    if !m[i][j] {
                        puntuaciones[i][j] = -1e10;
                    }
                }
            }
        }
        
        // Softmax
        let pesos_atencion = self.softmax(&puntuaciones);
        
        // Aplicar atención a valores
        let mut salida = vec![vec![0.0; dim_oculta]; longitud_seq];
        for i in 0..longitud_seq {
            for j in 0..longitud_seq {
                let peso = pesos_atencion[i][j];
                for d in 0..dim_oculta {
                    salida[i][d] += peso * v[j][d];
                }
            }
        }
        
        // Proyección de salida
        self.proyectar(&salida, &self.pesos_salida)
    }
    
    fn proyectar(&self, x: &[Vec<f32>], pesos: &[Vec<f32>]) -> Vec<Vec<f32>> {
        x.iter()
            .map(|fila| {
                pesos.iter()
                    .map(|peso_fila| {
                        fila.iter()
                            .zip(peso_fila.iter())
                            .map(|(a, b)| a * b)
                            .sum()
                    })
                    .collect()
            })
            .collect()
    }
    
    fn remodelar_cabezas(&self, x: &[Vec<f32>]) -> Vec<Vec<Vec<f32>>> {
        let longitud_seq = x.len();
        let mut cabezas = vec![vec![vec![0.0; self.dim_cabeza]; longitud_seq]; self.num_cabezas];
        
        for i in 0..longitud_seq {
            for h in 0..self.num_cabezas {
                for d in 0..self.dim_cabeza {
                    cabezas[h][i][d] = x[i][h * self.dim_cabeza + d];
                }
            }
        }
        
        cabezas
    }
    
    fn softmax(&self, x: &[Vec<f32>]) -> Vec<Vec<f32>> {
        x.iter()
            .map(|fila| {
                let max = fila.iter().cloned().fold(f32::NEG_INFINITY, f32::max);
                let exp_suma: f32 = fila.iter().map(|v| (v - max).exp()).sum();
                fila.iter().map(|v| (v - max).exp() / exp_suma).collect()
            })
            .collect()
    }
}

/// Bloque transformador español
pub struct BloqueTransformador {
    atencion: MotorAtencion,
    mlp: RedNeuronal,
    norm1: NormalizacionCapa,
    norm2: NormalizacionCapa,
}

impl BloqueTransformador {
    pub fn nuevo(config: &ConfiguracionGPT) -> Self {
        Self {
            atencion: MotorAtencion::nuevo(config.dim_oculta, config.num_cabezas),
            mlp: RedNeuronal::nueva(config.dim_oculta),
            norm1: NormalizacionCapa::nueva(config.dim_oculta),
            norm2: NormalizacionCapa::nueva(config.dim_oculta),
        }
    }
    
    pub fn adelante(&self, x: &[Vec<f32>], mascara: Option<&[Vec<bool>]>) -> Vec<Vec<f32>> {
        // Residual + atención
        let x_norm = self.norm1.adelante(x);
        let atencion_salida = self.atencion.adelante(&x_norm, mascara);
        let x_residual = self.agregar_residual(x, &atencion_salida);
        
        // Residual + MLP
        let x_norm2 = self.norm2.adelante(&x_residual);
        let mlp_salida = self.mlp.adelante(&x_norm2);
        self.agregar_residual(&x_residual, &mlp_salida)
    }
    
    fn agregar_residual(&self, x: &[Vec<f32>], residual: &[Vec<f32>]) -> Vec<Vec<f32>> {
        x.iter()
            .zip(residual.iter())
            .map(|(fila_x, fila_r)| {
                fila_x.iter()
                    .zip(fila_r.iter())
                    .map(|(a, b)| a + b)
                    .collect()
            })
            .collect()
    }
}

/// Red neuronal para procesamiento español
pub struct RedNeuronal {
    pesos1: Vec<Vec<f32>>,
    pesos2: Vec<Vec<f32>>,
    sesgo1: Vec<f32>,
    sesgo2: Vec<f32>,
}

impl RedNeuronal {
    pub fn nueva(dim_oculta: usize) -> Self {
        let dim_intermedia = dim_oculta * 4;
        
        Self {
            pesos1: MotorAtencion::inicializar_pesos(dim_oculta, dim_intermedia),
            pesos2: MotorAtencion::inicializar_pesos(dim_intermedia, dim_oculta),
            sesgo1: vec![0.0; dim_intermedia],
            sesgo2: vec![0.0; dim_oculta],
        }
    }
    
    pub fn adelante(&self, x: &[Vec<f32>]) -> Vec<Vec<f32>> {
        x.iter()
            .map(|fila| {
                // Primera capa con GELU
                let oculta: Vec<f32> = self.pesos1.iter()
                    .zip(self.sesgo1.iter())
                    .map(|(peso_fila, sesgo)| {
                        let suma: f32 = fila.iter()
                            .zip(peso_fila.iter())
                            .map(|(a, b)| a * b)
                            .sum::<f32>() + sesgo;
                        self.gelu(suma)
                    })
                    .collect();
                
                // Segunda capa
                self.pesos2.iter()
                    .zip(self.sesgo2.iter())
                    .map(|(peso_fila, sesgo)| {
                        oculta.iter()
                            .zip(peso_fila.iter())
                            .map(|(a, b)| a * b)
                            .sum::<f32>() + sesgo
                    })
                    .collect()
            })
            .collect()
    }
    
    fn gelu(&self, x: f32) -> f32 {
        0.5 * x * (1.0 + ((2.0 / std::f32::consts::PI).sqrt() * (x + 0.044715 * x.powi(3))).tanh())
    }
}

/// Normalización de capa
pub struct NormalizacionCapa {
    gamma: Vec<f32>,
    beta: Vec<f32>,
    epsilon: f32,
}

impl NormalizacionCapa {
    pub fn nueva(dim: usize) -> Self {
        Self {
            gamma: vec![1.0; dim],
            beta: vec![0.0; dim],
            epsilon: 1e-5,
        }
    }
    
    pub fn adelante(&self, x: &[Vec<f32>]) -> Vec<Vec<f32>> {
        x.iter()
            .map(|fila| {
                let media: f32 = fila.iter().sum::<f32>() / fila.len() as f32;
                let varianza: f32 = fila.iter()
                    .map(|v| (v - media).powi(2))
                    .sum::<f32>() / fila.len() as f32;
                
                fila.iter()
                    .zip(self.gamma.iter())
                    .zip(self.beta.iter())
                    .map(|((v, g), b)| {
                        ((v - media) / (varianza + self.epsilon).sqrt()) * g + b
                    })
                    .collect()
            })
            .collect()
    }
}

/// Núcleo GPT principal en español
pub struct NucleoGPTEspañol {
    pub config: ConfiguracionGPT,
    pub bloques: Vec<BloqueTransformador>,
    pub incrustacion_tokens: Vec<Vec<f32>>,
    pub incrustacion_posicion: Vec<Vec<f32>>,
    pub norm_final: NormalizacionCapa,
    pub cabeza_lm: Vec<Vec<f32>>,
    pub estado_emocional: EstadoEmocional,
    pub buffer_contexto: VecDeque<Vec<f32>>,
}

impl NucleoGPTEspañol {
    pub fn nuevo(config: ConfiguracionGPT) -> Self {
        let mut bloques = Vec::new();
        for _ in 0..config.num_capas {
            bloques.push(BloqueTransformador::nuevo(&config));
        }
        
        Self {
            bloques,
            incrustacion_tokens: Self::inicializar_incrustaciones(
                config.tamaño_vocabulario,
                config.dim_oculta
            ),
            incrustacion_posicion: Self::inicializar_incrustaciones(
                config.longitud_contexto,
                config.dim_oculta
            ),
            norm_final: NormalizacionCapa::nueva(config.dim_oculta),
            cabeza_lm: MotorAtencion::inicializar_pesos(config.dim_oculta, config.tamaño_vocabulario),
            estado_emocional: EstadoEmocional::default(),
            buffer_contexto: VecDeque::with_capacity(config.longitud_contexto),
            config,
        }
    }
    
    fn inicializar_incrustaciones(num: usize, dim: usize) -> Vec<Vec<f32>> {
        (0..num)
            .map(|_| {
                (0..dim)
                    .map(|_| rand::random::<f32>() * 0.02 - 0.01)
                    .collect()
            })
            .collect()
    }
    
    pub fn adelante(&mut self, tokens: &[usize]) -> Result<Vec<Vec<f32>>> {
        let _longitud_seq = tokens.len();
        
        // Incrustaciones de tokens + posición
        let mut x: Vec<Vec<f32>> = Vec::new();
        for (i, &token) in tokens.iter().enumerate() {
            let mut incrustacion = self.incrustacion_tokens[token].clone();
            for j in 0..self.config.dim_oculta {
                incrustacion[j] += self.incrustacion_posicion[i][j];
            }
            x.push(incrustacion);
        }
        
        // Aplicar abandono emocional
        x = self.aplicar_abandono_emocional(x);
        
        // Pasar por bloques transformadores
        for bloque in &self.bloques {
            x = bloque.adelante(&x, None);
        }
        
        // Normalización final
        x = self.norm_final.adelante(&x);
        
        // Cabeza de modelado de lenguaje
        let logits = self.aplicar_cabeza_lm(&x);
        
        // Actualizar contexto
        self.actualizar_contexto(&x);
        
        Ok(logits)
    }
    
    fn aplicar_abandono_emocional(&self, mut x: Vec<Vec<f32>>) -> Vec<Vec<f32>> {
        let intensidad_emocional = self.estado_emocional.activacion * self.estado_emocional.pasion;
        let prob_mantener = 1.0 - (self.config.tasa_abandono * (1.0 - intensidad_emocional));
        
        for fila in &mut x {
            for valor in fila {
                if rand::random::<f32>() > prob_mantener {
                    *valor = 0.0;
                }
            }
        }
        
        x
    }
    
    fn aplicar_cabeza_lm(&self, x: &[Vec<f32>]) -> Vec<Vec<f32>> {
        x.iter()
            .map(|fila| {
                self.cabeza_lm.iter()
                    .map(|peso_fila| {
                        fila.iter()
                            .zip(peso_fila.iter())
                            .map(|(a, b)| a * b)
                            .sum()
                    })
                    .collect()
            })
            .collect()
    }
    
    fn actualizar_contexto(&mut self, x: &[Vec<f32>]) {
        for fila in x {
            self.buffer_contexto.push_back(fila.clone());
            if self.buffer_contexto.len() > self.config.longitud_contexto {
                self.buffer_contexto.pop_front();
            }
        }
    }
    
    pub fn generar(&mut self, prompt: &[usize], max_tokens: usize) -> Result<Vec<usize>> {
        let mut tokens = prompt.to_vec();
        
        for _ in 0..max_tokens {
            let logits = self.adelante(&tokens)?;
            let siguiente_token = self.muestrear_con_emocion(&logits[logits.len() - 1]);
            tokens.push(siguiente_token);
        }
        
        Ok(tokens)
    }
    
    fn muestrear_con_emocion(&self, logits: &[f32]) -> usize {
        // Ajustar temperatura basada en estado emocional
        let temp = self.config.temp_emocional * 
                   (1.0 + self.estado_emocional.expresividad * 0.5) *
                   (1.0 + self.estado_emocional.pasion * 0.3);
        
        // Aplicar temperatura y softmax
        let max_logit = logits.iter().cloned().fold(f32::NEG_INFINITY, f32::max);
        let exp_logits: Vec<f32> = logits.iter()
            .map(|l| ((l - max_logit) / temp).exp())
            .collect();
        let suma: f32 = exp_logits.iter().sum();
        let probs: Vec<f32> = exp_logits.iter().map(|e| e / suma).collect();
        
        // Muestrear
        let mut aleatorio = rand::random::<f32>();
        for (i, &prob) in probs.iter().enumerate() {
            aleatorio -= prob;
            if aleatorio <= 0.0 {
                return i;
            }
        }
        
        probs.len() - 1
    }
    
    pub fn actualizar_emocion(&mut self, nueva_emocion: EstadoEmocional) {
        // Mezclar con estado actual para transición suave
        self.estado_emocional.valencia = 
            self.estado_emocional.valencia * 0.7 + nueva_emocion.valencia * 0.3;
        self.estado_emocional.activacion = 
            self.estado_emocional.activacion * 0.7 + nueva_emocion.activacion * 0.3;
        self.estado_emocional.dominancia = 
            self.estado_emocional.dominancia * 0.7 + nueva_emocion.dominancia * 0.3;
        self.estado_emocional.expresividad = 
            self.estado_emocional.expresividad * 0.6 + nueva_emocion.expresividad * 0.4;
        self.estado_emocional.pasion = 
            self.estado_emocional.pasion * 0.6 + nueva_emocion.pasion * 0.4;
    }
}

// Re-exportar para uso público
pub use self::{
    ConfiguracionGPT as GPTConfig,
    EstadoEmocional as EmotionalState,
    NucleoGPTEspañol as SpanishGPTCore,
};