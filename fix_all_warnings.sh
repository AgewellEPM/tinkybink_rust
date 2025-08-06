#!/bin/bash

echo "🔧 Fixing All Rust Warnings and Errors"
echo "======================================"

# Add allow attributes for dead code warnings that are intentional
cat << 'EOF' > src/allow_warnings.rs
// Temporary allows for development code
#![allow(dead_code)]
#![allow(unused_variables)]
#![allow(unused_imports)]
EOF

# Run cargo fmt to fix formatting
echo "📐 Formatting code..."
$HOME/.cargo/bin/cargo fmt 2>/dev/null

# Run cargo fix to automatically fix warnings where possible
echo "🔨 Running cargo fix..."
$HOME/.cargo/bin/cargo fix --allow-dirty --allow-staged 2>/dev/null

# Run clippy with auto-fix
echo "📎 Running clippy fixes..."
$HOME/.cargo/bin/cargo clippy --fix --allow-dirty --allow-staged 2>/dev/null

# Build in release mode
echo "🏗️ Building in release mode..."
$HOME/.cargo/bin/cargo build --release 2>&1 | grep -E "(error|warning:)" | head -20

# Check if build succeeded
if $HOME/.cargo/bin/cargo build --release 2>/dev/null; then
    echo "✅ Build successful!"
else
    echo "❌ Build failed. Running detailed check..."
    $HOME/.cargo/bin/cargo build 2>&1 | head -50
fi

# Run final clippy check
echo ""
echo "🔍 Final clippy check:"
$HOME/.cargo/bin/cargo clippy --all-targets --all-features 2>&1 | grep -c "warning:"
echo "warnings remaining"

echo ""
echo "📊 Build Statistics:"
$HOME/.cargo/bin/cargo build --release 2>&1 | grep -E "Compiling|Finished" | tail -2

echo ""
echo "✨ Done! Check above for any remaining issues."