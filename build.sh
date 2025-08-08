#!/usr/bin/env bash

function gw() {
    local file="./gradlew"
    if [[ -f "$file" ]]; then
        bash "$file" -Pandroid.aapt2FromMavenOverride="$HOME/.androidide/aapt2" "$@" 2>&1 | tee ./build.log
    else
        echo "Invoke this command from a project's root directory."
        return 1
    fi
}

gw "$@"