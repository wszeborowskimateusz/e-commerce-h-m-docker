FROM php:5.6-apache

RUN docker-php-ext-install pdo pdo_mysql

RUN apt-get update && apt-get install -y zlib1g-dev libicu-dev g++
RUN docker-php-ext-configure intl
RUN docker-php-ext-install intl
RUN a2enmod rewrite

RUN usermod -u 1000 www-data
RUN usermod -G staff www-data
RUN apt-get update && \
    apt-get install -y \
        zlib1g-dev && docker-php-ext-install zip
