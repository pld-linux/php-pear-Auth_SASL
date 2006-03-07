%include	/usr/lib/rpm/macros.php
%define		_class		Auth
%define		_subclass	SASL
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - generate responses to common SASL mechanisms
Summary(pl):	%{_pearname} - generowanie odpowiedzi dla popularnych mechanizmów SASL
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	5
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	9ed28f3f9bffc8265ea2339021f5dbf5
URL:		http://pear.php.net/package/Auth_SASL/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides code to generate responses to common SASL mechanisms,
including: Digest-MD5, CramMD5, Plain, Anonymous, Login (Pseudo
mechanism).

In PEAR status of this package is: %{_status}.

%description -l pl
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
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
