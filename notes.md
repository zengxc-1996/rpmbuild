## rpmbuild目录解释
```
BUILD：源代码解压以后放的位置，只需提供BUILD目录，具体里面放什么，不用我们管，所以真正的制作车间是BUILD目录。
BUILDROOT：假根，使用install临时安装到这个目录，把这个目录当作根来用的，所以在这个目录下的目录文件，才是真正的目录文件。当打包完成后，在清理阶段，这个目录将被删除。
RPMS：制作完成后的rpm包存放目录，为特定平台指定子目录（i386,i686,ppc）。
SOURCES：收集的源文件，源材料，补丁文件等存放位置。
SPECS：存放spec文件，作为制作rpm包的领岗文件，文件以.spec结尾。
SRPMS：src格式的rpm包位置 ，既然是src格式的包，就没有平台的概念了。
```

## spec文件详解
```
1、spec基本信息

    Name:                        软件名称
    Version:                     软件版本
    Release:                     发布次数    如: 1%{?dist}
    Summary:                     软件说明
    Group:                       软件分组
    License:                     授权模式,例如 GPL，即自由软件
    URL:                         源码包的URL地址，可随意填写
    Source0:                     源码包,可指定多个,下面可用%{SOURCE0}变量引用
    BuildRoot:                   编译过程中的中间存档目录，考虑到多用户的环境，一般定义为：
                                %{_tmppath}/%{name}-%{version}-%{release}-root ，
                                后面可使用$RPM_BUILD_ROOT 方式引用
    BuildArch:                   平台    %{_arch}
    BuildRequires:               编译过程依赖的工具
    Requires:                    打包生成的rpm包安装时所依赖的软件包
    %description                 说明文档
    %prep                        准备部分,比如创建目录,解压源码包等,可使用%setup内部函数
    %build                       在BUILD目录编译,可使用%configure内部函数,或者其他编译工具,如cmake, perl等
    %install                     安装到BUILDROOT虚拟目录
    %clean                       清理文件
    %files                       将指定的文件添加到rpm包中,文档类型可用%doc,配置文件可  用%config
    %changelog                   更新记录.格式: 第一行 "* 日期 作者 " 第二行 "- 更新内容"
    最终的生成的rpm名称: {Name}-{Version}-{Relesae}-{BuildArch}.rpm
```
```
常用内部变量:   
在spec文件运行时，定义的宏会主动读取/usr/lib/rpm/macros中的变量   
RPM_BUILD_DIR     ~/rpmbuild/BUILD  
RPM_BUILD_ROOT    ~/rpmbuild/BUILDROOT   
```

## 打包时生成debuginfo包?
```
可以用 echo '%debug_package %{nil}' >> ~/.rpmmacros 禁止该功能

```
