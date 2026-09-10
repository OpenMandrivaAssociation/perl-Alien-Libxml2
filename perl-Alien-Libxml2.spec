%define upstream_name    Alien-Libxml2
%define debug_package %{nil}
%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:	0.20
Release:    1

Summary:    Alien package for libxml2
License:    GPLv1+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/release/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Alien/%{upstream_name}-%{version}.tar.gz

BuildRequires:	make
BuildRequires: perl(Alien::Base)
BuildRequires: perl(Alien::Build)
BuildRequires: perl(Alien::Build::MM)
BuildRequires: perl(Alien::Build::Plugin::Build::SearchDep)
BuildRequires: perl(Alien::Build::Plugin::Prefer::BadVersion)
BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(ExtUtils::MakeMaker)
#BuildRequires: perl(Test2::V0)
#BuildRequires: perl(Test::Alien)
BuildRequires: pkgconfig(libxml-2.0)
Requires:   python-libxml2

%description
Alien::Libxml2 - Download and install libxml2

%prep
%setup -q -n Alien-Libxml2-0.20

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make_build

%install
%make_install

%files
%doc Changes INSTALL LICENSE META.json META.yml README
%{_mandir}/man3/*
%perl_vendorarch/*
