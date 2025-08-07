<p align="center">
  <img src="./images/icon.png" alt="AndroidIDE" width="80" height="80"/>
</p>

<h2 align="center"><b>AndroidIDE</b></h2>
<p align="center">
  AndroidIDE 是一个运行在安卓设备上的应用程序开发工具，支持完整的 Android SDK 和 Gradle。
<p><br>

<p align="center">
<!-- Latest release -->
<img src="https://img.shields.io/github/v/release/evil-hero/AndroidIDE-R?include_prereleases&amp;label=latest%20release" alt="Latest release">
<!-- Build and test -->
<img src="https://github.com/evil-hero/AndroidIDE-R/actions/workflows/build.yml/badge.svg" alt="Builds and tests">
<!-- CodeFactor -->
<img src="https://www.codefactor.io/repository/github/androidideofficial/androidide/badge/main" alt="CodeFactor">
<!-- Crowdin -->
<a href="https://crowdin.com/project/androidide"><img src="https://badges.crowdin.net/androidide/localized.svg" alt="Crowdin"></a>
<!-- License -->
<img src="https://img.shields.io/badge/License-GPLv3-blue.svg" alt="License"></p>

<p align="center">
  <a href="docs/README-SOURCE.md">查看官方文档 »</a> &nbsp; &nbsp;
  <a href="docs/README-EN.md">English Docs »</a> &nbsp; &nbsp;
</p>

<p align="center">
  <a href="https://github.com/evil-hero/AndroidIDE-R/issues/new?labels=bug&template=BUG.yml&title=%5BBug%5D%3A+">提交 Bug</a> &nbsp; &#8226; &nbsp;
  <a href="https://github.com/evil-hero/AndroidIDE-R/issues/new?labels=feature&template=FEATURE.yml&title=%5BFeature%5D%3A+">新功能建议</a> &nbsp; &#8226; &nbsp;
  <a href="https://t.me/androidide_r_discussions">加入TG群组</a>
</p>

> [!WARNING]
> 
> 暂时仅支持`arm64`架构的安卓设备安装。

## 功能速览


## 安装应用

- [_GitHub Releases_](https://github.com/evil-hero/AndroidIDE-R/releases)

## 应用限制

- 要在 AndroidIDE 中开发项目，您的项目必须使用 Android Gradle 插件 v7.2.0 或更高版本。使用旧版 AGP 的项目必须迁移到较新版本。

- SDK Manager 已经包含在 Android SDK 中，可通过 AndroidIDE 的终端访问。但是，您无法使用它来安装某些工具（例如 NDK）。

- 没有官方的 NDK 支持，因为有很多人使用 NDK 编译外挂程序。如果您真的需要 NDK 环境，可以考虑使用 Termux 搭建。

该应用仍在积极开发中。目前处于测试阶段，可能不稳定。如果您在使用该应用时遇到任何问题，请告知我们。

## 贡献指南

请查看 [贡献指南](./CONTRIBUTING.md)。

> [!NOTE]
> 
> 暂不进行翻译工作。

## 鸣谢

- [Rosemoe](https://github.com/Rosemoe) 的优秀代码编辑器 [CodeEditor](https://github.com/Rosemoe/sora-editor)
- [Termux](https://github.com/termux) 的超级终端 [Terminal Emulator](https://github.com/termux/termux-app)
- [Bogdan Melnychuk](https://github.com/bmelnychuk)
  的树状组件 [AndroidTreeView](https://github.com/bmelnychuk/AndroidTreeView)
- [George Fraser](https://github.com/georgewfraser) 的 Java  语言服务器 [Java Language Server](https://github.com/georgewfraser/java-language-server)

感谢所有为该项目做出贡献的开发人员。

## 联系我们

- [Telegram](https://t.me/androidide_r_discussions)

## License

```
AndroidIDE is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

AndroidIDE is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with AndroidIDE.  If not, see <https://www.gnu.org/licenses/>.
```

任何违反许可证的行为都可以通过任何方式告知我们。