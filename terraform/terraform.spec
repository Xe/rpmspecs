name:           terraform
Version:        0.6.14
Release:        0%{?dist}
Summary:        INFRASTRUCTURE AS CODE
ExclusiveArch:  x86_64

URL:            https://terraform.io
License:        Apache License, Version 2.0
Group:          System Environment/Daemons

Source0:        terraform_0.6.14_linux_amd64.zip

%description
Terraform provides a common configuration to launch infrastructure — from physical and virtual servers to email and DNS providers. Once launched, Terraform safely and efficiently changes infrastructure as the configuration is evolved.

Simple file based configuration gives you a single view of your entire infrastructure.
%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post %{nil}

%prep
%setup -c

%build
#Nothing to do here.

%install
mkdir -p %{buildroot}/%{_bindir}

cp -a terraform %{buildroot}/%{_bindir}
cp -a terraform-provider-atlas %{buildroot}/%{_bindir}
cp -a terraform-provider-aws %{buildroot}/%{_bindir}
cp -a terraform-provider-azure %{buildroot}/%{_bindir}
cp -a terraform-provider-azurerm %{buildroot}/%{_bindir}
cp -a terraform-provider-chef %{buildroot}/%{_bindir}
cp -a terraform-provider-clc %{buildroot}/%{_bindir}
cp -a terraform-provider-cloudflare %{buildroot}/%{_bindir}
cp -a terraform-provider-cloudstack %{buildroot}/%{_bindir}
cp -a terraform-provider-consul %{buildroot}/%{_bindir}
cp -a terraform-provider-datadog %{buildroot}/%{_bindir}
cp -a terraform-provider-digitalocean %{buildroot}/%{_bindir}
cp -a terraform-provider-dme %{buildroot}/%{_bindir}
cp -a terraform-provider-dnsimple %{buildroot}/%{_bindir}
cp -a terraform-provider-docker %{buildroot}/%{_bindir}
cp -a terraform-provider-dyn %{buildroot}/%{_bindir}
cp -a terraform-provider-github %{buildroot}/%{_bindir}
cp -a terraform-provider-google %{buildroot}/%{_bindir}
cp -a terraform-provider-heroku %{buildroot}/%{_bindir}
cp -a terraform-provider-influxdb %{buildroot}/%{_bindir}
cp -a terraform-provider-mailgun %{buildroot}/%{_bindir}
cp -a terraform-provider-mysql %{buildroot}/%{_bindir}
cp -a terraform-provider-null %{buildroot}/%{_bindir}
cp -a terraform-provider-openstack %{buildroot}/%{_bindir}
cp -a terraform-provider-packet %{buildroot}/%{_bindir}
cp -a terraform-provider-postgresql %{buildroot}/%{_bindir}
cp -a terraform-provider-powerdns %{buildroot}/%{_bindir}
cp -a terraform-provider-rundeck %{buildroot}/%{_bindir}
cp -a terraform-provider-statuscake %{buildroot}/%{_bindir}
cp -a terraform-provider-template %{buildroot}/%{_bindir}
cp -a terraform-provider-terraform %{buildroot}/%{_bindir}
cp -a terraform-provider-tls %{buildroot}/%{_bindir}
cp -a terraform-provider-triton %{buildroot}/%{_bindir}
cp -a terraform-provider-ultradns %{buildroot}/%{_bindir}
cp -a terraform-provider-vcd %{buildroot}/%{_bindir}
cp -a terraform-provider-vsphere %{buildroot}/%{_bindir}
cp -a terraform-provisioner-chef %{buildroot}/%{_bindir}
cp -a terraform-provisioner-file %{buildroot}/%{_bindir}
cp -a terraform-provisioner-local-exec %{buildroot}/%{_bindir}
cp -a terraform-provisioner-remote-exec %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(755, root, root) %{_bindir}/terraform
%attr(755, root, root) %{_bindir}/terraform-provider-atlas
%attr(755, root, root) %{_bindir}/terraform-provider-aws
%attr(755, root, root) %{_bindir}/terraform-provider-azure
%attr(755, root, root) %{_bindir}/terraform-provider-azurerm
%attr(755, root, root) %{_bindir}/terraform-provider-chef
%attr(755, root, root) %{_bindir}/terraform-provider-clc
%attr(755, root, root) %{_bindir}/terraform-provider-cloudflare
%attr(755, root, root) %{_bindir}/terraform-provider-cloudstack
%attr(755, root, root) %{_bindir}/terraform-provider-consul
%attr(755, root, root) %{_bindir}/terraform-provider-datadog
%attr(755, root, root) %{_bindir}/terraform-provider-digitalocean
%attr(755, root, root) %{_bindir}/terraform-provider-dme
%attr(755, root, root) %{_bindir}/terraform-provider-dnsimple
%attr(755, root, root) %{_bindir}/terraform-provider-docker
%attr(755, root, root) %{_bindir}/terraform-provider-dyn
%attr(755, root, root) %{_bindir}/terraform-provider-github
%attr(755, root, root) %{_bindir}/terraform-provider-google
%attr(755, root, root) %{_bindir}/terraform-provider-heroku
%attr(755, root, root) %{_bindir}/terraform-provider-influxdb
%attr(755, root, root) %{_bindir}/terraform-provider-mailgun
%attr(755, root, root) %{_bindir}/terraform-provider-mysql
%attr(755, root, root) %{_bindir}/terraform-provider-null
%attr(755, root, root) %{_bindir}/terraform-provider-openstack
%attr(755, root, root) %{_bindir}/terraform-provider-packet
%attr(755, root, root) %{_bindir}/terraform-provider-postgresql
%attr(755, root, root) %{_bindir}/terraform-provider-powerdns
%attr(755, root, root) %{_bindir}/terraform-provider-rundeck
%attr(755, root, root) %{_bindir}/terraform-provider-statuscake
%attr(755, root, root) %{_bindir}/terraform-provider-template
%attr(755, root, root) %{_bindir}/terraform-provider-terraform
%attr(755, root, root) %{_bindir}/terraform-provider-tls
%attr(755, root, root) %{_bindir}/terraform-provider-triton
%attr(755, root, root) %{_bindir}/terraform-provider-ultradns
%attr(755, root, root) %{_bindir}/terraform-provider-vcd
%attr(755, root, root) %{_bindir}/terraform-provider-vsphere
%attr(755, root, root) %{_bindir}/terraform-provisioner-chef
%attr(755, root, root) %{_bindir}/terraform-provisioner-file
%attr(755, root, root) %{_bindir}/terraform-provisioner-local-exec
%attr(755, root, root) %{_bindir}/terraform-provisioner-remote-exec

%changelog
* Mon Apr 18 2016 Christine Dodrill <me@christine.website>
- Initial packaging
