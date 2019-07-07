%define upstream_name    Alien-Libxml2
%define upstream_version 0.09

%define debug_package %{nil}
%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Alien package for libxml2
License:    GPLv1+ or Artistic
Group:      Development/Perl
Url:        http://metacpan.org/release/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Alien/%{upstream_name}-%{upstream_version}.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make_build

%install
%make_install

%files
%doc Changes INSTALL LICENSE META.json META.yml README
%{_mandir}/man3/*
%perl_vendorarch/*
