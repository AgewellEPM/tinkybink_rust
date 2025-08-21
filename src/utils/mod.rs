use chrono::{DateTime, Utc};
use std::time::{SystemTime, UNIX_EPOCH};

/// Utility functions for the TinkyBink AAC system
///
/// Get current timestamp as UTC DateTime
pub fn current_timestamp() -> DateTime<Utc> {
    Utc::now()
}

/// Get current timestamp as Unix timestamp
pub fn current_unix_timestamp() -> u64 {
    SystemTime::now().duration_since(UNIX_EPOCH).unwrap_or_default().as_secs()
}

/// Format duration in a human-readable way
pub fn format_duration(seconds: u64) -> String {
    if seconds < 60 {
        format!("{seconds}s")
    } else if seconds < 3600 {
        format!("{}m {}s", seconds / 60, seconds % 60)
    } else {
        format!("{}h {}m", seconds / 3600, (seconds % 3600) / 60)
    }
}

/// Sanitize text for safe display and storage
pub fn sanitize_text(text: &str) -> String {
    text.chars()
        .filter(|c| c.is_alphabetic() || c.is_numeric() || c.is_whitespace() || ".,!?-".contains(*c))
        .collect::<String>()
        .trim()
        .to_string()
}

/// Calculate confidence score for speech recognition results
pub fn calculate_confidence(raw_confidence: f32, length: usize, noise_level: f32) -> f32 {
    let mut confidence = raw_confidence;

    // Adjust for length (very short or very long phrases are less reliable)
    if length < 3 {
        confidence *= 0.8;
    } else if length > 50 {
        confidence *= 0.9;
    }

    // Adjust for noise level
    confidence *= 1.0 - noise_level * 0.3;

    // Clamp to valid range
    confidence.clamp(0.0, 1.0)
}
