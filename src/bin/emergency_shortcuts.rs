// Emergency Shortcut System for Critical AAC Situations
// Provides instant access to emergency responses with single tap

use serde::{Deserialize, Serialize};
use std::collections::HashMap;

#[derive(Debug, Serialize, Deserialize)]
pub struct EmergencyResponse {
    pub icon: String,
    pub label: String,
    pub message: String,
    pub urgency: UrgencyLevel,
    pub actions: Vec<EmergencyAction>,
}

#[derive(Debug, Serialize, Deserialize)]
pub enum UrgencyLevel {
    Critical,  // Life-threatening - immediate response needed
    High,      // Severe discomfort - quick response needed  
    Medium,    // Moderate issue - timely response needed
    Low,       // Minor issue - can wait
}

#[derive(Debug, Serialize, Deserialize)]
pub enum EmergencyAction {
    CallNurse,
    Call911,
    AlertFamily,
    SendLocation,
    PlayAlarm,
    FlashScreen,
    TextToSpeech(String),
}

pub struct EmergencyShortcutSystem {
    shortcuts: HashMap<String, EmergencyResponse>,
}

impl EmergencyShortcutSystem {
    pub fn new() -> Self {
        let mut shortcuts = HashMap::new();
        
        // CRITICAL MEDICAL EMERGENCIES - Red Zone
        shortcuts.insert("chest_pain".to_string(), EmergencyResponse {
            icon: "🚨".to_string(),
            label: "CHEST PAIN".to_string(),
            message: "I'm having severe chest pain! Call 911 immediately!".to_string(),
            urgency: UrgencyLevel::Critical,
            actions: vec![
                EmergencyAction::Call911,
                EmergencyAction::AlertFamily,
                EmergencyAction::PlayAlarm,
                EmergencyAction::TextToSpeech("Emergency! Chest pain! Call 911!".to_string()),
            ],
        });
        
        shortcuts.insert("cant_breathe".to_string(), EmergencyResponse {
            icon: "🫁".to_string(),
            label: "CAN'T BREATHE".to_string(),
            message: "I can't breathe! Need help immediately!".to_string(),
            urgency: UrgencyLevel::Critical,
            actions: vec![
                EmergencyAction::Call911,
                EmergencyAction::CallNurse,
                EmergencyAction::PlayAlarm,
                EmergencyAction::FlashScreen,
            ],
        });
        
        shortcuts.insert("stroke_symptoms".to_string(), EmergencyResponse {
            icon: "🧠".to_string(),
            label: "STROKE".to_string(),
            message: "I think I'm having a stroke! Face drooping, arm weak, speech difficult!".to_string(),
            urgency: UrgencyLevel::Critical,
            actions: vec![
                EmergencyAction::Call911,
                EmergencyAction::TextToSpeech("Stroke symptoms! Call 911! Time is critical!".to_string()),
                EmergencyAction::AlertFamily,
            ],
        });
        
        shortcuts.insert("severe_bleeding".to_string(), EmergencyResponse {
            icon: "🩸".to_string(),
            label: "BLEEDING".to_string(),
            message: "Severe bleeding! Need immediate medical help!".to_string(),
            urgency: UrgencyLevel::Critical,
            actions: vec![
                EmergencyAction::CallNurse,
                EmergencyAction::Call911,
                EmergencyAction::PlayAlarm,
            ],
        });
        
        // HIGH URGENCY - Orange Zone
        shortcuts.insert("severe_pain".to_string(), EmergencyResponse {
            icon: "😰".to_string(),
            label: "SEVERE PAIN".to_string(),
            message: "I'm in severe pain! Please get help quickly!".to_string(),
            urgency: UrgencyLevel::High,
            actions: vec![
                EmergencyAction::CallNurse,
                EmergencyAction::TextToSpeech("Severe pain! Need help!".to_string()),
                EmergencyAction::AlertFamily,
            ],
        });
        
        shortcuts.insert("fallen".to_string(), EmergencyResponse {
            icon: "🚑".to_string(),
            label: "I FELL".to_string(),
            message: "I've fallen and need help getting up!".to_string(),
            urgency: UrgencyLevel::High,
            actions: vec![
                EmergencyAction::CallNurse,
                EmergencyAction::SendLocation,
                EmergencyAction::TextToSpeech("I've fallen! Need assistance!".to_string()),
            ],
        });
        
        shortcuts.insert("allergic_reaction".to_string(), EmergencyResponse {
            icon: "🤧".to_string(),
            label: "ALLERGIC".to_string(),
            message: "I'm having an allergic reaction!".to_string(),
            urgency: UrgencyLevel::High,
            actions: vec![
                EmergencyAction::CallNurse,
                EmergencyAction::TextToSpeech("Allergic reaction! Need medication!".to_string()),
            ],
        });
        
        shortcuts.insert("bathroom_urgent".to_string(), EmergencyResponse {
            icon: "🚽".to_string(),
            label: "BATHROOM NOW".to_string(),
            message: "I need the bathroom urgently! Can't wait!".to_string(),
            urgency: UrgencyLevel::High,
            actions: vec![
                EmergencyAction::CallNurse,
                EmergencyAction::TextToSpeech("Bathroom emergency! Please help now!".to_string()),
            ],
        });
        
        // MEDIUM URGENCY - Yellow Zone
        shortcuts.insert("medication_time".to_string(), EmergencyResponse {
            icon: "💊".to_string(),
            label: "MEDICINE".to_string(),
            message: "I need my medication now.".to_string(),
            urgency: UrgencyLevel::Medium,
            actions: vec![
                EmergencyAction::CallNurse,
                EmergencyAction::TextToSpeech("Time for medication please.".to_string()),
            ],
        });
        
        shortcuts.insert("feeling_sick".to_string(), EmergencyResponse {
            icon: "🤢".to_string(),
            label: "FEEL SICK".to_string(),
            message: "I feel nauseous and might throw up.".to_string(),
            urgency: UrgencyLevel::Medium,
            actions: vec![
                EmergencyAction::CallNurse,
                EmergencyAction::TextToSpeech("Feeling sick, need help.".to_string()),
            ],
        });
        
        shortcuts.insert("too_hot".to_string(), EmergencyResponse {
            icon: "🥵".to_string(),
            label: "TOO HOT".to_string(),
            message: "I'm overheating! Need cooling immediately!".to_string(),
            urgency: UrgencyLevel::Medium,
            actions: vec![
                EmergencyAction::CallNurse,
                EmergencyAction::TextToSpeech("Too hot! Need cooling!".to_string()),
            ],
        });
        
        shortcuts.insert("panic_attack".to_string(), EmergencyResponse {
            icon: "😱".to_string(),
            label: "PANIC".to_string(),
            message: "I'm having a panic attack! Need calming help!".to_string(),
            urgency: UrgencyLevel::Medium,
            actions: vec![
                EmergencyAction::CallNurse,
                EmergencyAction::AlertFamily,
                EmergencyAction::TextToSpeech("Panic attack, need calming assistance.".to_string()),
            ],
        });
        
        Self { shortcuts }
    }
    
    pub fn get_all_shortcuts(&self) -> Vec<(String, &EmergencyResponse)> {
        let mut shortcuts: Vec<_> = self.shortcuts.iter()
            .map(|(k, v)| (k.clone(), v))
            .collect();
        
        // Sort by urgency level (Critical first)
        shortcuts.sort_by(|a, b| {
            match (&a.1.urgency, &b.1.urgency) {
                (UrgencyLevel::Critical, UrgencyLevel::Critical) => std::cmp::Ordering::Equal,
                (UrgencyLevel::Critical, _) => std::cmp::Ordering::Less,
                (_, UrgencyLevel::Critical) => std::cmp::Ordering::Greater,
                (UrgencyLevel::High, UrgencyLevel::High) => std::cmp::Ordering::Equal,
                (UrgencyLevel::High, _) => std::cmp::Ordering::Less,
                (_, UrgencyLevel::High) => std::cmp::Ordering::Greater,
                (UrgencyLevel::Medium, UrgencyLevel::Medium) => std::cmp::Ordering::Equal,
                (UrgencyLevel::Medium, _) => std::cmp::Ordering::Less,
                (_, UrgencyLevel::Medium) => std::cmp::Ordering::Greater,
                _ => std::cmp::Ordering::Equal,
            }
        });
        
        shortcuts
    }
    
    pub fn trigger_emergency(&self, shortcut_id: &str) -> Option<&EmergencyResponse> {
        self.shortcuts.get(shortcut_id)
    }
    
    pub fn get_critical_shortcuts(&self) -> Vec<(&String, &EmergencyResponse)> {
        self.shortcuts.iter()
            .filter(|(_, response)| matches!(response.urgency, UrgencyLevel::Critical))
            .collect()
    }
}

// iOS Integration Helper
#[derive(Serialize)]
pub struct IOSEmergencyTile {
    pub id: String,
    pub icon: String,
    pub label: String,
    pub color: String,  // Red, Orange, Yellow based on urgency
    pub flash: bool,    // Should tile flash for attention
}

impl EmergencyShortcutSystem {
    pub fn get_ios_tiles(&self) -> Vec<IOSEmergencyTile> {
        self.get_all_shortcuts().into_iter().map(|(id, response)| {
            let (color, flash) = match response.urgency {
                UrgencyLevel::Critical => ("#FF0000".to_string(), true),   // Red, flashing
                UrgencyLevel::High => ("#FF8C00".to_string(), false),      // Orange
                UrgencyLevel::Medium => ("#FFD700".to_string(), false),    // Gold
                UrgencyLevel::Low => ("#90EE90".to_string(), false),       // Light green
            };
            
            IOSEmergencyTile {
                id,
                icon: response.icon.clone(),
                label: response.label.clone(),
                color,
                flash,
            }
        }).collect()
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_emergency_shortcuts() {
        let system = EmergencyShortcutSystem::new();
        
        // Test critical shortcut exists
        let chest_pain = system.trigger_emergency("chest_pain");
        assert!(chest_pain.is_some());
        assert!(matches!(chest_pain.unwrap().urgency, UrgencyLevel::Critical));
        
        // Test getting all critical shortcuts
        let critical = system.get_critical_shortcuts();
        assert!(critical.len() >= 4); // At least 4 critical emergencies
        
        // Test iOS tiles generation
        let tiles = system.get_ios_tiles();
        assert!(!tiles.is_empty());
        
        // Verify critical tiles are red and flash
        let critical_tile = tiles.iter().find(|t| t.id == "chest_pain").unwrap();
        assert_eq!(critical_tile.color, "#FF0000");
        assert!(critical_tile.flash);
    }
}

fn main() {
    let emergency_system = EmergencyShortcutSystem::new();
    
    println!("🚨 EMERGENCY AAC SHORTCUT SYSTEM 🚨");
    println!("=====================================\n");
    
    println!("CRITICAL EMERGENCIES (Red Zone - Immediate Action):");
    println!("──────────────────────────────────────────────────");
    for (id, response) in emergency_system.get_critical_shortcuts() {
        println!("{} {} - {}", response.icon, response.label, id);
        println!("   Message: {}", response.message);
        println!("   Actions: {:?}\n", response.actions);
    }
    
    println!("\nALL EMERGENCY SHORTCUTS:");
    println!("────────────────────────");
    for (id, response) in emergency_system.get_all_shortcuts() {
        let urgency_color = match response.urgency {
            UrgencyLevel::Critical => "🔴",
            UrgencyLevel::High => "🟠",
            UrgencyLevel::Medium => "🟡",
            UrgencyLevel::Low => "🟢",
        };
        println!("{} {} {} - {}", urgency_color, response.icon, response.label, response.message);
    }
    
    // Simulate iOS integration
    println!("\n📱 iOS EMERGENCY TILES:");
    println!("─────────────────────");
    let ios_tiles = emergency_system.get_ios_tiles();
    for tile in ios_tiles.iter().take(6) {
        println!("{} {} [{}] {}", 
            tile.icon, 
            tile.label, 
            tile.color,
            if tile.flash { "⚡FLASHING⚡" } else { "" }
        );
    }
    
    println!("\n✅ Emergency shortcut system ready for integration!");
}