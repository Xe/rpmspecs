%global commit      922237d7f35e1bcb974b161760cc953a97ebcafe
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           macarena
Version:        0.5
Release:        6%{?dist}
Summary:        An IRC bot for communities spanning networks.
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
export GOPATH=$(pwd):$(pwd)/vendor
function gobuild { go build -a -ldflags "-B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \n')" -v -x "$@"; }
cd src/cmd/macarena
gobuild ./...
cp macarena ../../..

%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 macarena %{buildroot}%{_bindir}/macarena

%files
%defattr(-,root,root,-)
%doc UNLICENSE README.md
%{_bindir}/macarena

%changelog
* Sat May 09 2015 Xena <xena@yolo-swag.com> - 0.5
- package macarena

