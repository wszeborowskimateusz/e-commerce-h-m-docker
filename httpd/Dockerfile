FROM php:5.6-apache

RUN docker-php-ext-install pdo pdo_mysql
RUN a2enmod rewrite

USER root
COPY ./prestashop /src
RUN rm -rf /var/www/html && mv /src /var/www/html &&\
    chmod -R 777 /var/www
