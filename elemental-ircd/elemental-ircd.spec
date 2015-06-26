%define user_group  ircd

%global _hardened_build 1

Name:       elemental-ircd
Version:    6.6.2
Release:    1%{?dist}
Summary:    A high performance, lightweight and scalable IRC daemon

License:    GPLv2
Group:      System Environment/Daemons

Conflicts:  ircd-hybrid
BuildRequires:  openssl-devel, bison, flex, systemd, chrpath
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires(pre):  shadow-utils

URL:        https://github.com/Elemental-IRCd/elemental-ircd
Source0:    https://github.com/Elemental-IRCd/elemental-ircd/archive/elemental-ircd-%{version}.tar.gz
Source1:    ircd.service
Source2:    ircd.conf

%description
Elemental-IRCd is a high performance, lightweight, and scalable IRC daemon.
It is a fork of the now-defunct ShadowIRCD and seeks to continue in the
direction ShadowIRCD was headed.

%prep
%setup -q -n elemental-ircd-elemental-ircd-%{version}

%configure \
    --bindir=%{_bindir} \
    --sbindir=%{_sbindir} \
    --with-helpdir=%{_datadir}/ircd \
    --with-moduledir=%{_datadir}/ircd/modules \
    --with-confdir=%{_sysconfdir}/ircd \
    --mandir=%{_mandir} \
    --with-logdir=%{_var}/log/ircd \
    --enable-ipv6 \
    --enable-openssl \
    --enable-zlib \
    --with-nicklen=32 \
    --with-topiclen=350 \
    --disable-rpath

%build
make %{?_smp_mflags} CFLAGS="-O0 -Wall -std=gnu99 -g -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -m64 -mtune=generic -lpthread"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_sbindir} $RPM_BUILD_ROOT%{_datadir}/ircd $RPM_BUILD_ROOT%{_var}/log $RPM_BUILD_ROOT%{_sysconfdir}/ircd
make install DESTDIR=$RPM_BUILD_ROOT

install -D -m644 %{SOURCE1} $RPM_BUILD_ROOT/%{_unitdir}/ircd.service
install -D -m644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/ircd/ircd.conf

mv $RPM_BUILD_ROOT%{_datadir}/ircd-old/modules $RPM_BUILD_ROOT%{_datadir}/ircd/modules
rm -fr $RPM_BUILD_ROOT%{_datadir}/ircd-old
mkdir -p $RPM_BUILD_ROOT/run/elemental-ircd

rm $RPM_BUILD_ROOT%{_bindir}/convertklines
rm $RPM_BUILD_ROOT%{_bindir}/convertilines
rm $RPM_BUILD_ROOT%{_bindir}/viconf
rm $RPM_BUILD_ROOT%{_bindir}/mkpasswd
rm $RPM_BUILD_ROOT%{_bindir}/vimotd
rm $RPM_BUILD_ROOT%{_bindir}/bantool
rm $RPM_BUILD_ROOT%{_bindir}/genssl.sh

chrpath --delete $RPM_BUILD_ROOT%{_bindir}/ircd
chrpath --delete $RPM_BUILD_ROOT/usr/libexec/elemental-ircd/ssld
chrpath --delete $RPM_BUILD_ROOT/usr/libexec/elemental-ircd/bandb

%clean
rm -rf $RPM_BUILD_ROOT

%pre
getent group ircd  >/dev/null || groupadd -r ircd
getent passwd ircd >/dev/null || \
useradd -r -g ircd -d /run/elemental-ircd -s /sbin/nologin \
    -c "elemental-ircd user" ircd

%post
%systemd_post ircd.service

%preun
%systemd_preun ircd.service

%postun
%systemd_postun_with_restart ircd.service

%files
%doc CREDITS INSTALL LICENSE README.md doc/*
%{_bindir}/ircd
%{_datadir}/ircd*
/usr/libexec/elemental-ircd/*
%dir %{_sysconfdir}/ircd
%config(noreplace) %{_sysconfdir}/ircd/*
%{_unitdir}/ircd.service
%doc %{_mandir}/man8/ircd*
%dir %attr(750,ircd,ircd) %{_var}/log/ircd
%dir %attr(750,ircd,ircd) /run/elemental-ircd
/usr/lib64/libratbox.la
/usr/lib64/libratbox.so
/usr/lib64/pkgconfig/libratbox.pc


%changelog
* Fri Jun 26 2015 Christine Dodrill <me@christine.website> - 6.6.2
- Initial packaging
