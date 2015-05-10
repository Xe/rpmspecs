%global commit      922237d7f35e1bcb974b161760cc953a97ebcafe
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           macarena
Version:        0.5
Release:        6%{?dist}
Summary:        This application is an example for the golang binary RPM spec
License:        Unlicense
URL:            https://github.com/Xe/macarena
Source0:        https://github.com/Xe/macarena/archive/v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  golang >= 1.2-7

# pull in golang libraries by explicit import path, inside the meta golang()

%description
Macarena is a relay bot for IRC channels spanning many networks. It runs simply and leaves as little state as possible.

%prep
%setup -q -n macarena-%{version}

%build
# set up temporary build gopath, and put our directory there
mkdir -p ./_build/src/

export GOPATH=$(pwd)/_build:%{gopath}
go get github.com/constabulary/gb/...
$(pwd)/_build/bin/gb build

%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 ./bin/macarena %{buildroot}%{_bindir}/example-app

%files
%defattr(-,root,root,-)
%doc UNLICENSE README.md
%{_bindir}/bin/macarena

%changelog
* Sat May 09 2015 Xena <xena@yolo-swag.com> - 0.5
- package macarena

