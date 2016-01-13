name:           otto
Version:        0.2.0
Release:        0%{?dist}
Summary:        Infrastructure tool
ExclusiveArch:  x86_64

URL:            https://ottoproject.io
License:        Apache License, Version 2.0
Group:          System Environment/Daemons

Source0:        otto_0.2.0_linux_amd64.zip

%description
Otto knows how to develop and deploy any application on any cloud platform, all controlled with a single consistent workflow to maximize the productivity of you and your team.

%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post %{nil}

%prep
%setup -c 

%build
#Nothing to do here.

%install
mkdir -p %{buildroot}/%{_bindir}
cp -a otto %{buildroot}/%{_bindir}/otto

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(755, root, root) %{_bindir}/otto

%changelog
* Wed Jan 13 2016 Christine Dodrill <me@christine.website>
- Initial packaging
