%include	/usr/lib/rpm/macros.perl
%define	pdir	Language
%define	pnam	DATR-DATR2XML
Summary:	Language::DATR::DATR2XML perl module
Summary(pl):	Modu³ perla Language::DATR::DATR2XML
Name:		perl-Language-DATR-DATR2XML
Version:	0.901
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-libwww
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The DATR2XML package is a colleciton of files to provide XML support
for Sussex-standard DATR.

%description -l pl
Pakiet DATR2XML to zestaw plików maj±cych za zadanie dodanie obs³ugi
XML do DATR w standardzie Sussex.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.txt thanks.txt XML-XSLT
%{perl_vendorlib}/Language/DATR
%{_mandir}/man3/*
