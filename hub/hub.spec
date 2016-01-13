Name:           hub
Version:        2.2.2
Release:        0%{?dist}
Summary:        Github command line tool
ExclusiveArch:  x86_64

URL:            https://github.com/github/hub
License:        Apache License, Version 2.0
Group:          System Environment/Daemons

Source0:        hub-linux-amd64-2.2.2.tgz

%description
git + hub = github
hub is a command line tool that wraps git in order to extend it with extra features and commands that make working with GitHub easier.

$ hub clone rtomayko/tilt

expands to:

$ git clone git://github.com/rtomayko/tilt.git

hub is best aliased as git, so you can type $ git <command> in the shell and get all the usual hub features.

%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post %{nil}

%prep
%setup -c 

%build
#Nothing to do here.

%install
mkdir -p %{buildroot}/%{_bindir}
cp -a hub-linux-amd64-2.2.2/bin/hub %{buildroot}/%{_bindir}/hub

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(755, root, root) %{_bindir}/hub

%doc hub-linux-amd64-2.2.2/README.md
%license hub-linux-amd64-2.2.2/LICENSE
%{!?_licensedir:%global license %doc}

%changelog
* Tue Jan 12 2016 Christine Dodrill <me@christine.website>
- Initial packaging
