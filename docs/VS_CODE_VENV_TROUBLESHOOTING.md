# VS Code Virtual Environment Troubleshooting Guide

## Why Does My Venv Quit Running in VS Code?

Virtual environments in VS Code can "quit" due to several configuration issues. Here's how to fix them:

## 🔧 **Quick Fixes**

### **1. Enable Terminal Persistence**
VS Code terminals need to persist between sessions:

```json
// In .vscode/settings.json
"terminal.integrated.enablePersistentSessions": true
```

### **2. Simplify Terminal Profile**
Complex terminal startup commands can fail. Use this simple profile:

```json
// In .vscode/settings.json
"terminal.integrated.profiles.windows": {
    "PowerShell": {
        "source": "PowerShell",
        "icon": "terminal-powershell",
        "args": ["-NoExit"]
    }
}
```

### **3. Manual Activation**
When terminal opens, run:
```powershell
. .\activate_venv.ps1
```

## 🐛 **Common Issues & Solutions**

### **Issue: Terminal closes immediately**
**Cause**: Complex startup commands failing
**Fix**: Simplify terminal profile (see above)

### **Issue: Venv activates but disappears**
**Cause**: `enablePersistentSessions: false`
**Fix**: Set to `true` in settings

### **Issue: "Cannot find path" errors**
**Cause**: Working directory issues
**Fix**: Ensure you're in the project root directory

### **Issue: Python interpreter not found**
**Cause**: VS Code not using venv Python
**Fix**: Check `python.defaultInterpreterPath` in settings

## 🚀 **Recommended VS Code Setup**

### **Settings.json Configuration**
```json
{
    "python.defaultInterpreterPath": ".venv\\Scripts\\python.exe",
    "terminal.integrated.enablePersistentSessions": true,
    "terminal.integrated.profiles.windows": {
        "PowerShell": {
            "source": "PowerShell",
            "icon": "terminal-powershell",
            "args": ["-NoExit"]
        }
    }
}
```

### **Workflow**
1. Open VS Code in project root
2. Open terminal (Ctrl+`)
3. Run: `. .\activate_venv.ps1`
4. Terminal stays active with venv

## 🔍 **Diagnostic Commands**

### **Check Venv Status**
```powershell
.\check_venv.ps1
```

### **Test Python**
```powershell
python --version
which python
```

### **Check Environment Variables**
```powershell
$env:VIRTUAL_ENV
$env:PATH
```

## 🛠️ **Advanced Troubleshooting**

### **Reset VS Code Terminal**
1. Close all terminals (Terminal → Close All Terminals)
2. Reload VS Code (Ctrl+Shift+P → "Developer: Reload Window")
3. Open new terminal

### **Rebuild Virtual Environment**
```batch
.\rebuild_venv_safe.bat
```

### **Check VS Code Logs**
1. Help → Toggle Developer Tools
2. Check Console for errors

## 📋 **Prevention Tips**

1. **Always use persistent terminals**: Keep `enablePersistentSessions: true`
2. **Avoid complex terminal profiles**: Keep startup commands simple
3. **Use manual activation**: Run `. .\activate_venv.ps1` when needed
4. **Check venv regularly**: Run `.\check_venv.ps1` to verify status

## 🎯 **If Issues Persist**

1. Try a different terminal profile (Command Prompt instead of PowerShell)
2. Disable all VS Code extensions temporarily
3. Reset VS Code settings to defaults
4. Reinstall VS Code (last resort)

The most common fix is enabling persistent sessions and simplifying the terminal profile!