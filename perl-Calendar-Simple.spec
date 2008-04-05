#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Calendar
%define		pnam	Simple
Summary:	Calendar::Simple - Perl extension to create simple calendars
Summary(pl.UTF-8):	Calendar::Simple - rozszerzenie Perla do tworzenia prostych kalendarzy
Name:		perl-Calendar-Simple
Version:	1.19
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Calendar/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b4f974f74f615b8aadfdba43b3a646f1
URL:		http://search.cpan.org/dist/Calendar-Simple/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl extension to create simple calendars.

%description -l pl.UTF-8
Rozszerzenie Perla do tworzenia prostych kalendarzy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%dir %{perl_vendorlib}/Calendar
%{perl_vendorlib}/Calendar/*.pm
%{_mandir}/man3/*
