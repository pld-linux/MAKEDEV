#
# Conditional build:
%bcond_without	selinux		# build without SELinux support
#
Summary:	Program to make and update /dev entries
Summary(de.UTF-8):   Script zum Erstellen und Aktualisieren von /dev-Einträgen
Summary(es.UTF-8):   Script para hacer y actualizar entradas referentes a dispositivos en /dev
Summary(fr.UTF-8):   Script pour créer et mettre à jour les entrées /dev
Summary(pl.UTF-8):   Program do tworzenia i poprawiania urządzeń z /dev
Summary(pt_BR.UTF-8):   Script para fazer e atualizar entradas referentes a dispositivos em /dev
Summary(tr.UTF-8):   Aygıt tanımı yapmak ve değiştirmek için bir araç
Name:		MAKEDEV
Version:	3.13
Release:	2
License:	GPL v2+
Group:		Applications/System
Source0:	%{name}-%{version}-1.tar.gz
# Source0-md5:	f8befaebd0813c6fa59c07ef3875f232
Patch0:		%{name}-ub.patch
%if %{with selinux}
BuildRequires:	libselinux-devel >= 0:1.8
Requires:	libselinux >= 0:1.8
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		/sbin

%description
The /dev tree holds special files, each of which corresponds to a type
of hardware device that Linux supports. This package contains a
program which makes it easier to create and maintain the files which
fill the /dev tree.

%description -l de.UTF-8
Die /dev-Hierarchie enthält spezielle Dateien, von denen jede einem
Hardwaregerättyp entspricht, der von Linux unterstützt wird. Dieses
Paket enthält ein Skript, das die Erstellung und die Pflege der
Dateien innerhalb dieser Hierarchie vereinfacht.

%description -l es.UTF-8
El directorio /dev posee archivos especiales, cada uno de ellos
correspondiendo a un tipo de dispositivo de hardware que Linux
soporta. Este paquete contiene un script que hace más fácil la
creación y manutención de los archivos en el directorio /dev.

%description -l fr.UTF-8
L'arborescence /dev contient des fichiers spéciaux. Chacun d'eux
correspond à un périphérique matériel gérable par Linux. Ce paquetage
contient un script facilitant la création et la maintenance des
fichiers qui remplissent l'arborescence /dev.

%description -l pl.UTF-8
Pliki specjalne znajdujące się w katalogu /dev odpowiadają
urządzeniom, które są obsługiwane przez Linuksa. Pakiet ten zawiera
program, który uczyni tworzenie i operowanie tymi plikami łatwiejszym.

%description -l pt_BR.UTF-8
O diretório /dev possui arquivos especiais, cada um deles
correspondendo a um tipo de dispositivo de hardware que o Linux
suporta. Este pacote contém um script que torna mais fácil a criação
e manutenção dos arquivos no diretório /dev.

%description -l tr.UTF-8
Unix ve Unix benzeri sistemler (Linux da dahil olmak üzere), makinaya
bağlı aygıtları göstermek için özel dosyalar kullanırlar. Bu özel
dosyaların tümü /dev dizin yapısı altındadır. Bu paket en çok
kullanılan /dev dosyalarını içerir. Bu dosyalar, bir sistemin düzgün
olarak işleyebilmesi için temel gereksinimlerdendir.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags} %{rpmldflags}" \
	%{?with_selinux:SELINUX=1}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	devdir=/dev \
	makedevdir=/sbin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/MAKEDEV
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
%config %{_sysconfdir}/makedev.d
