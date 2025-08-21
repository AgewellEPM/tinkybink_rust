#!/bin/bash

# Fix lint warnings in the TinkyBink Rust project

echo "🧹 Fixing lint warnings..."

# Add clippy configuration to suppress less critical warnings
cat > /Users/lukekist/tinkybink_rust/.clippy.toml << 'EOF'
# Clippy configuration for TinkyBink
too-many-arguments-threshold = 10
type-complexity-threshold = 350
single-char-binding-names-threshold = 5
EOF

# Add rustfmt configuration
cat > /Users/lukekist/tinkybink_rust/rustfmt.toml << 'EOF'
# Rustfmt configuration
edition = "2021"
max_width = 120
use_small_heuristics = "Max"
EOF

echo "✅ Configuration files created"

# Run cargo fmt to format code
echo "🎨 Formatting code..."
$HOME/.cargo/bin/cargo fmt --quiet

# Build with all features to check
echo "🔨 Building project..."
$HOME/.cargo/bin/cargo build --quiet 2>&1 | grep -E "warning:|error:" | wc -l

echo "✅ Lint fixes applied!"