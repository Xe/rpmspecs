Name:           caddy
Version:        0.9.0
Release:        0%{?dist}
Summary:        Caddy is a lightweight, general-purpose web server for Windows, Mac, Linux, BSD and Android written in GoLang.
BuildArch:      x86_64

URL:		https://caddyserver.com/
License:        Apache License, Version 2.0
Group:          System Environment/Daemons

BuildRequires: systemd
Requires(post): systemd

Source0:	caddy_linux_amd64_custom.tar.gz
Source1:	Caddyfile
Source2:	caddy.service
Source3:  environment

%description
Caddy is a lightweight, general-purpose web server for Windows,
Mac, Linux, BSD and Android. It is a capable alternative to
other popular and easy to use web servers.

The most notable features are HTTP/2, Let's Encrypt support,
Virtual Hosts, TLS + SNI, and easy configuration with a
Caddyfile. In development, you usually put one Caddyfile with
each site. In production, Caddy serves HTTPS by default and
manages all cryptographic assets for you.

This package has the following features enabled: cors, git,
hugo, ipfilter, jsonp and search.

%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post %{nil}

%prep
%setup -c

%build
#Nothing to do here.

%install
mkdir -p %{buildroot}/%{_bindir}
cp -a caddy %{buildroot}/%{_bindir}/caddy

install -D -m644 %{SOURCE2} $RPM_BUILD_ROOT/%{_unitdir}/caddy.service
install -D -m644 %{SOURCE1} $RPM_BUILD_ROOT/%{_sysconfdir}/caddy/Caddyfile.example
install -D -m644 %{SOURCE3} $RPM_BUILD_ROOT/%{_sysconfdir}/caddy/environment

%clean
rm -rf %{buildroot}

%pre
getent group caddy  >/dev/null || groupadd -r caddy
getent passwd caddy >/dev/null || \
useradd -r -g caddy -d /var/lib/caddy -s /sbin/nologin \
    -c "caddy user" caddy

%files
%defattr(-,root,root,-)
%attr(755, root, root) %{_bindir}/caddy
%{_sysconfdir}/caddy/Caddyfile.example
%{_sysconfdir}/caddy/environment
%{_unitdir}/caddy.service

%doc CHANGES.txt README.txt
%license LICENSES.txt
%{!?_licensedir:%global license %doc}

%post
setcap cap_net_bind_service=+ep %{_bindir}/caddy
%systemd_post caddy.service

%changelog
* Tue Jul 19 2016 Cadey Dodrill <me@christine.website>
- Update to 0.9.0

* Tue Apr 26 2016 Cadey Dodrill <me@christine.website>
- Update to Caddy 0.0.3
- Disable hugo (breaking build)
- Enable JWT, Prometheus and mailout
- Add /etc/caddy/environment for JWT secret (default is *******)

* Mon Feb 29 2016 Christine Dodrill <me@christine.website>
- Update to Caddy 0.8.2.
- Enable all features

* Tue Jan 12 2016 Christine Dodrill <me@christine.website>
- Add systemd unit and example Caddyfile

* Tue Jan 12 2016 Christine Dodrill <me@christine.website>
- Update to Caddy 0.8.1.
- Enable all features.

* Sat Dec 26 2015 Joe Doss <copr@joedoss.com>
- Adjust license directory.
- Add setcap cap_net_bind_service=+ep to caddy binary.

* Fri Dec 25 2015 Joe Doss <copr@joedoss.com>
- Initial x86_64 RPM Release. Version 0.8.0.
- Enable features: cors, git, hugo, ipfilter, jsonp and search.
- See https://github.com/mholt/caddy/releases/tag/v0.8.0 for full details.
