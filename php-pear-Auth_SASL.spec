%define		_status		stable
%define		_pearname	Auth_SASL
Summary:	%{_pearname} - generate responses to common SASL mechanisms
Summary(pl.UTF-8):	%{_pearname} - generowanie odpowiedzi dla popularnych mechanizmów SASL
Name:		php-pear-%{_pearname}
Version:	1.1.0
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	dc2641c4d64e4ebe3f0076d412ee4126
URL:		http://pear.php.net/package/Auth_SASL/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides code to generate responses to common SASL mechanisms,
including: Digest-MD5, CramMD5, Plain, Anonymous, Login (Pseudo
mechanism).

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ta klasa udostępnia kod do generowania odpowiedzi dla popularnych
mechanizmów SASL, w tym: Digest-MD5, CramMD5, Plain, Anonymous, Login
(Pseudo mechanizm).

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/Auth/SASL
%{php_pear_dir}/Auth/*.php
%{php_pear_dir}/Auth/SASL/*.php
