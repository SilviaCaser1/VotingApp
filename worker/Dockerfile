# Usamos la imagen base de .NET SDK para construir la app
FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build

# Define el directorio de trabajo
WORKDIR /app

# Copia el archivo del proyecto y restaura dependencias
COPY worker.csproj ./
RUN dotnet restore worker.csproj

# Copia el resto del código y compila la aplicación
COPY . ./
RUN dotnet publish -c Release -o /app/publish --no-restore

# Usa una imagen más ligera para la ejecución
FROM mcr.microsoft.com/dotnet/aspnet:7.0 AS runtime
WORKDIR /app
COPY --from=build /app/publish .

# Expone el puerto en el que escucha la app (ajustalo si es diferente)
EXPOSE 5000

# Comando de inicio
ENTRYPOINT ["dotnet", "worker.dll"]
