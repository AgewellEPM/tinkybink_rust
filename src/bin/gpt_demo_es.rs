//! 🇪🇸 Demo de GPT en Español - Sistema AAC Inteligente
//!
//! Demuestra el poder del núcleo GPT español con:
//! - Procesamiento de lenguaje natural en español
//! - Conciencia emocional y cultural
//! - Patrones conversacionales españoles
//! - Integración con datos de entrenamiento

use anyhow::Result;
use colored::*;
use serde_json::Value;
use std::fs;
use std::io::{self, Write};
use std::path::Path;
use tinkybink_rust::ai::gpt_core_es::{ConfiguracionGPT, EstadoEmocional, NucleoGPTEspañol};

/// Cargador de datos de entrenamiento españoles
struct CargadorDatosEspañol {
    vocabulario: Vec<String>,
    frases: Vec<Vec<String>>,
    emociones: Vec<EstadoEmocional>,
}

impl CargadorDatosEspañol {
    fn nuevo() -> Result<Self> {
        let mut vocabulario = Vec::new();
        let mut frases = Vec::new();
        let mut emociones = Vec::new();

        // Cargar todos los archivos de entrenamiento españoles
        let dir_entrenamiento = Path::new("training_es");
        if dir_entrenamiento.exists() {
            for entrada in fs::read_dir(dir_entrenamiento)? {
                let entrada = entrada?;
                let ruta = entrada.path();
                if ruta.extension().and_then(|s| s.to_str()) == Some("json") {
                    let contenido = fs::read_to_string(&ruta)?;
                    let datos: Value = serde_json::from_str(&contenido)?;

                    if let Some(nodos) = datos["nodes"].as_array() {
                        for nodo in nodos {
                            // Extraer texto
                            if let Some(texto) = nodo["text"].as_str() {
                                let palabras: Vec<String> = texto.split_whitespace().map(|s| s.to_string()).collect();
                                frases.push(palabras.clone());
                                for palabra in palabras {
                                    if !vocabulario.contains(&palabra) {
                                        vocabulario.push(palabra);
                                    }
                                }
                            }

                            // Extraer emociones
                            if let Some(emocion) = nodo["emotion"].as_object() {
                                let estado = EstadoEmocional {
                                    valencia: emocion.get("valencia").and_then(|v| v.as_f64()).unwrap_or(0.5) as f32,
                                    activacion: emocion.get("activacion").and_then(|v| v.as_f64()).unwrap_or(0.5)
                                        as f32,
                                    dominancia: emocion.get("dominancia").and_then(|v| v.as_f64()).unwrap_or(0.5)
                                        as f32,
                                    expresividad: emocion.get("expresividad").and_then(|v| v.as_f64()).unwrap_or(0.7)
                                        as f32,
                                    pasion: emocion.get("pasion").and_then(|v| v.as_f64()).unwrap_or(0.6) as f32,
                                };
                                emociones.push(estado);
                            }
                        }
                    }
                }
            }
        }

        // Si no hay datos, usar ejemplos por defecto
        if vocabulario.is_empty() {
            vocabulario = vec![
                "Hola", "Buenos", "días", "¿Cómo", "estás?", "Muy", "bien", "gracias", "Por", "favor", "Necesito",
                "ayuda", "Tengo", "hambre", "sed", "Me", "duele", "Quiero", "jugar", "mamá", "papá", "escuela", "casa",
                "amigo", "feliz", "triste", "¡Olé!", "¡Vamos!", "¿Qué", "tal?", "Adiós", "Hasta", "luego",
            ]
            .iter()
            .map(|s| s.to_string())
            .collect();
        }

        Ok(Self { vocabulario, frases, emociones })
    }

    fn tokenizar(&self, texto: &str) -> Vec<usize> {
        texto.split_whitespace().filter_map(|palabra| self.vocabulario.iter().position(|v| v == palabra)).collect()
    }

    fn detokenizar(&self, tokens: &[usize]) -> String {
        tokens.iter().filter_map(|&idx| self.vocabulario.get(idx)).cloned().collect::<Vec<_>>().join(" ")
    }
}

/// Demo interactiva principal
fn ejecutar_demo() -> Result<()> {
    println!("{}", "╔══════════════════════════════════════════════════════════╗".cyan());
    println!("{}", "║     🇪🇸 TINKYBINK GPT ESPAÑOL - SISTEMA AAC INTELIGENTE    ║".cyan().bold());
    println!("{}", "╚══════════════════════════════════════════════════════════╝".cyan());
    println!();

    // Cargar datos de entrenamiento
    println!("{} Cargando datos de entrenamiento españoles...", "→".green());
    let cargador = CargadorDatosEspañol::nuevo()?;
    println!("{} Vocabulario: {} palabras", "✓".green(), cargador.vocabulario.len());
    println!("{} Frases de entrenamiento: {}", "✓".green(), cargador.frases.len());
    println!("{} Estados emocionales: {}", "✓".green(), cargador.emociones.len());
    println!();

    // Configurar el modelo
    let config = ConfiguracionGPT {
        tamaño_vocabulario: cargador.vocabulario.len().max(1000),
        dim_oculta: 256,
        num_capas: 6,
        num_cabezas: 8,
        longitud_contexto: 512,
        tasa_abandono: 0.1,
        temp_emocional: 0.8,
    };

    println!("{} Inicializando núcleo GPT español...", "→".yellow());
    let mut modelo = NucleoGPTEspañol::nuevo(config);
    println!("{} ¡Modelo listo!", "✓".green().bold());
    println!();

    // Menú de demostración
    loop {
        println!("{}", "┌─────────────────────────────────────┐".magenta());
        println!("{}", "│       MENÚ DE DEMOSTRACIÓN          │".magenta().bold());
        println!("{}", "├─────────────────────────────────────┤".magenta());
        println!("{}", "│ 1. Generar saludo español           │".magenta());
        println!("{}", "│ 2. Expresar necesidad básica        │".magenta());
        println!("{}", "│ 3. Mostrar emoción cultural         │".magenta());
        println!("{}", "│ 4. Conversación interactiva         │".magenta());
        println!("{}", "│ 5. Demostración de pasión española  │".magenta());
        println!("{}", "│ 6. Emergencia médica                │".magenta());
        println!("{}", "│ 0. Salir                            │".magenta());
        println!("{}", "└─────────────────────────────────────┘".magenta());

        print!("\n{} Elige una opción: ", "→".cyan());
        io::stdout().flush()?;

        let mut entrada = String::new();
        io::stdin().read_line(&mut entrada)?;

        match entrada.trim() {
            "1" => demostrar_saludo(&mut modelo, &cargador)?,
            "2" => demostrar_necesidad(&mut modelo, &cargador)?,
            "3" => demostrar_emocion(&mut modelo, &cargador)?,
            "4" => conversacion_interactiva(&mut modelo, &cargador)?,
            "5" => demostrar_pasion(&mut modelo, &cargador)?,
            "6" => demostrar_emergencia(&mut modelo, &cargador)?,
            "0" => {
                println!("\n{} ¡Adiós! ¡Hasta la vista!", "👋".to_string().yellow());
                break;
            }
            _ => println!("{} Opción no válida", "✗".red()),
        }

        println!();
    }

    Ok(())
}

fn demostrar_saludo(modelo: &mut NucleoGPTEspañol, cargador: &CargadorDatosEspañol) -> Result<()> {
    println!("\n{}", "=== GENERACIÓN DE SALUDO ESPAÑOL ===".green().bold());

    // Establecer estado emocional alegre y expresivo
    modelo.actualizar_emocion(EstadoEmocional {
        valencia: 0.9,
        activacion: 0.7,
        dominancia: 0.6,
        expresividad: 0.9,
        pasion: 0.8,
    });

    let prompts = vec!["Buenos", "Hola", "¿Qué"];

    for prompt in prompts {
        let tokens = cargador.tokenizar(prompt);
        if !tokens.is_empty() {
            let generado = modelo.generar(&tokens, 5)?;
            let texto = cargador.detokenizar(&generado);
            println!("{} {} → {}", "💬".to_string(), prompt.yellow(), texto.green());
        }
    }

    Ok(())
}

fn demostrar_necesidad(modelo: &mut NucleoGPTEspañol, cargador: &CargadorDatosEspañol) -> Result<()> {
    println!("\n{}", "=== EXPRESIÓN DE NECESIDADES ===".blue().bold());

    // Estado emocional de necesidad
    modelo.actualizar_emocion(EstadoEmocional {
        valencia: 0.3,
        activacion: 0.8,
        dominancia: 0.4,
        expresividad: 0.8,
        pasion: 0.5,
    });

    let necesidades = vec!["Tengo", "Necesito", "Quiero"];

    for necesidad in necesidades {
        let tokens = cargador.tokenizar(necesidad);
        if !tokens.is_empty() {
            let generado = modelo.generar(&tokens, 4)?;
            let texto = cargador.detokenizar(&generado);
            println!("{} {} → {}", "🆘".to_string(), necesidad.yellow(), texto.cyan());
        }
    }

    Ok(())
}

fn demostrar_emocion(modelo: &mut NucleoGPTEspañol, cargador: &CargadorDatosEspañol) -> Result<()> {
    println!("\n{}", "=== EXPRESIONES EMOCIONALES CULTURALES ===".magenta().bold());

    let emociones = vec![
        (
            "Feliz",
            EstadoEmocional { valencia: 1.0, activacion: 0.9, dominancia: 0.7, expresividad: 1.0, pasion: 0.9 },
            "😄",
        ),
        (
            "Triste",
            EstadoEmocional { valencia: 0.1, activacion: 0.3, dominancia: 0.2, expresividad: 0.6, pasion: 0.4 },
            "😢",
        ),
        (
            "Apasionado",
            EstadoEmocional { valencia: 0.8, activacion: 1.0, dominancia: 0.9, expresividad: 1.0, pasion: 1.0 },
            "🔥",
        ),
    ];

    for (nombre, emocion, emoji) in emociones {
        modelo.actualizar_emocion(emocion);
        let tokens = cargador.tokenizar("Me");
        if !tokens.is_empty() {
            let generado = modelo.generar(&tokens, 6)?;
            let texto = cargador.detokenizar(&generado);
            println!("{} {} → {}", emoji, nombre.yellow(), texto.magenta());
        }
    }

    Ok(())
}

fn conversacion_interactiva(modelo: &mut NucleoGPTEspañol, cargador: &CargadorDatosEspañol) -> Result<()> {
    println!("\n{}", "=== CONVERSACIÓN INTERACTIVA ===".cyan().bold());
    println!("{}", "Escribe en español (o 'salir' para terminar)".italic());

    loop {
        print!("\n{} Tú: ", "👤".to_string());
        io::stdout().flush()?;

        let mut entrada = String::new();
        io::stdin().read_line(&mut entrada)?;
        let entrada = entrada.trim();

        if entrada == "salir" {
            break;
        }

        // Analizar emoción de la entrada
        let emocion = analizar_emocion_entrada(entrada);
        modelo.actualizar_emocion(emocion);

        let tokens = cargador.tokenizar(entrada);
        if !tokens.is_empty() {
            let generado = modelo.generar(&tokens, 8)?;
            let respuesta = cargador.detokenizar(&generado);
            println!("{} TinkyBink: {}", "🤖".to_string(), respuesta.green());
        } else {
            println!("{} TinkyBink: {}", "🤖".to_string(), "No entiendo, ¿puedes repetir?".yellow());
        }
    }

    Ok(())
}

fn demostrar_pasion(modelo: &mut NucleoGPTEspañol, cargador: &CargadorDatosEspañol) -> Result<()> {
    println!("\n{}", "=== DEMOSTRACIÓN DE PASIÓN ESPAÑOLA ===".red().bold());

    // Máxima pasión y expresividad
    modelo.actualizar_emocion(EstadoEmocional {
        valencia: 0.9,
        activacion: 1.0,
        dominancia: 0.8,
        expresividad: 1.0,
        pasion: 1.0,
    });

    let expresiones = vec!["¡Olé!", "¡Vamos!", "¡Qué"];

    for expr in expresiones {
        let tokens = cargador.tokenizar(expr);
        if !tokens.is_empty() {
            let generado = modelo.generar(&tokens, 6)?;
            let texto = cargador.detokenizar(&generado);
            println!("{} {} → {}", "💃".to_string(), expr.red(), texto.yellow().bold());
        }
    }

    Ok(())
}

fn demostrar_emergencia(modelo: &mut NucleoGPTEspañol, cargador: &CargadorDatosEspañol) -> Result<()> {
    println!("\n{}", "=== SITUACIÓN DE EMERGENCIA ===".red().bold().on_yellow());

    // Estado de urgencia
    modelo.actualizar_emocion(EstadoEmocional {
        valencia: 0.1,
        activacion: 1.0,
        dominancia: 0.3,
        expresividad: 1.0,
        pasion: 0.9,
    });

    let emergencias = vec!["¡Ayuda!", "Me duele", "Necesito médico"];

    for emergencia in emergencias {
        let tokens = cargador.tokenizar(emergencia);
        if !tokens.is_empty() {
            let generado = modelo.generar(&tokens, 5)?;
            let texto = cargador.detokenizar(&generado);
            println!("{} {} → {}", "🚨".to_string(), emergencia.red().bold(), texto.on_red().white());
        }
    }

    println!("\n{} Llamando al 112...", "📞".to_string().blink());

    Ok(())
}

fn analizar_emocion_entrada(texto: &str) -> EstadoEmocional {
    let texto_lower = texto.to_lowercase();

    // Análisis básico de sentimiento
    let palabras_positivas = ["feliz", "bien", "genial", "estupendo", "alegre", "contento"];
    let palabras_negativas = ["triste", "mal", "dolor", "miedo", "enfadado", "cansado"];
    let palabras_urgentes = ["ayuda", "emergencia", "dolor", "necesito", "urgente"];
    let palabras_pasionales = ["ole", "vamos", "increíble", "amor", "pasión"];

    let mut valencia: f32 = 0.5;
    let mut activacion: f32 = 0.5;
    let mut expresividad: f32 = 0.7;
    let mut pasion: f32 = 0.6;

    for palabra in palabras_positivas.iter() {
        if texto_lower.contains(palabra) {
            valencia += 0.2;
            activacion += 0.1;
        }
    }

    for palabra in palabras_negativas.iter() {
        if texto_lower.contains(palabra) {
            valencia -= 0.2;
            activacion += 0.1;
        }
    }

    for palabra in palabras_urgentes.iter() {
        if texto_lower.contains(palabra) {
            activacion = 1.0;
            expresividad = 1.0;
        }
    }

    for palabra in palabras_pasionales.iter() {
        if texto_lower.contains(palabra) {
            pasion = 1.0;
            expresividad = 1.0;
        }
    }

    // Signos de exclamación aumentan la expresividad
    let exclamaciones = texto.matches('!').count() as f32;
    expresividad = (expresividad + exclamaciones * 0.1).min(1.0);
    pasion = (pasion + exclamaciones * 0.05).min(1.0);

    EstadoEmocional {
        valencia: valencia.clamp(0.0, 1.0),
        activacion: activacion.clamp(0.0, 1.0),
        dominancia: 0.5,
        expresividad: expresividad.clamp(0.0, 1.0),
        pasion: pasion.clamp(0.0, 1.0),
    }
}

fn main() {
    println!(
        "{}",
        "
╔═══════════════════════════════════════════════════════════════════╗
║                                                                    ║
║   ████████╗██╗███╗   ██╗██╗  ██╗██╗   ██╗██████╗ ██╗███╗   ██╗██╗  ██╗  ║
║   ╚══██╔══╝██║████╗  ██║██║ ██╔╝╚██╗ ██╔╝██╔══██╗██║████╗  ██║██║ ██╔╝  ║
║      ██║   ██║██╔██╗ ██║█████╔╝  ╚████╔╝ ██████╔╝██║██╔██╗ ██║█████╔╝   ║
║      ██║   ██║██║╚██╗██║██╔═██╗   ╚██╔╝  ██╔══██╗██║██║╚██╗██║██╔═██╗   ║
║      ██║   ██║██║ ╚████║██║  ██╗   ██║   ██████╔╝██║██║ ╚████║██║  ██╗  ║
║      ╚═╝   ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝   ╚═════╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝  ║
║                                                                    ║
║                  🇪🇸 GPT ESPAÑOL - EDICIÓN ESPECIAL 🇪🇸                ║
║                                                                    ║
╚═══════════════════════════════════════════════════════════════════╝
    "
        .bright_red()
        .bold()
    );

    if let Err(e) = ejecutar_demo() {
        eprintln!("{} Error: {}", "✗".red().bold(), e);
        std::process::exit(1);
    }
}
