%include	/usr/lib/rpm/macros.php
%define		_class		Auth
%define		_subclass	SASL
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - generate responses to common SASL mechanisms
Summary(pl):	%{_pearname} - generowanie odpowiedzi dla popularnych mechanizmów SASL
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	4
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	9ed28f3f9bffc8265ea2339021f5dbf5
URL:		http://pear.php.net/package/Auth_SASL/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides code to generate responses to common SASL mechanisms,
including: Digest-MD5, CramMD5, Plain, Anonymous, Login (Pseudo
mechanism).

In PEAR status of this package is: %{_status}.

%description -l pl
Ta klasa udostêpnia kod do generowania odpowiedzi dla popularnych
mechanizmów SASL, w tym: Digest-MD5, CramMD5, Plain, Anonymous, Login
(Pseudo mechanizm).

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
