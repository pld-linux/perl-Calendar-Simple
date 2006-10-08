#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Calendar
%define		pnam	Simple
Summary:	Calendar::Simple - Perl extension to create simple calendars
Summary(pl):	Calendar::Simple - rozszerzenie Perla do tworzenia prostych kalendarzy
Name:		perl-%{pdir}-%{pnam}
Version:	1.14
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b6a9fb7194b9657a8e3932032809fbc3
URL:		http://search.cpan.org/dist/Carp-Clan/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl extension to create simple calendars.

%description -l pl
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
