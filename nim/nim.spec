Name: nim
Group: Development/Languages
Version: 0.13.0
Release: 2%{?dist}
Summary: A compiled, garbage-collected systems programming language
License: MIT
Source0: http://nim-lang.org/download/%{name}-%{version}.tar.xz
Patch0: 2969.patch
URL: http://nim-lang.org

BuildRequires: pcre-devel

%description
Nim (formerly known as "Nimrod") is a compiled, garbage-collected systems programming language which has an excellent
productivity/performance ratio. Nim's design focuses on efficiency, expressiveness, elegance (in the order of priority).

%prep
%setup -q
%patch0 -p1

%build
./build.sh

%install
%{__rm} -rf %{buildroot}
./install.sh %{buildroot}

%{__mkdir_p} %{buildroot}%{_datadir}/nim
%{__mkdir_p} %{buildroot}%{_prefix}/lib

%{__mv} %{buildroot}/nim/bin                     %{buildroot}%{_bindir}
%{__mv} %{buildroot}/nim/config                  %{buildroot}%{_sysconfdir}
%{__mv} %{buildroot}/nim/lib                     %{buildroot}%{_prefix}/lib/nim
%{__mv} %{buildroot}/nim/doc                     %{buildroot}%{_datadir}/nim/doc

%check
#./bin/nim c koch
#PATH=./bin:$PATH ./koch tests --pedantic category lib

%files
%defattr(-,root,root)
%{_bindir}/nim
%{_prefix}/lib/nim/*
%config %{_sysconfdir}/*.cfg
%doc %{_datadir}/nim/doc/*


%changelog
* Mon Jan 18 2016 Christine Dodrill <me@christine.website> - 0.13.0
- Update to 0.13.0

* Tue Jan 12 2016 Christine Dodrill <me@christine.website> - 0.12.0
- Update to 0.12.0

* Sun May 24 2015 Sergey Avseyev <sergey.avseyev@gmail.com> - 0.11.2
- Initial package
