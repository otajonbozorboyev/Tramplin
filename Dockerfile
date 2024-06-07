FROM python:3.11
ENV PYTHONUNBUFFERED 1
# PYTHONUNBUFFERED bu narsa bufferlangan holatini o'chirib qo'yadi yani bufferlangan holatida malumotlarni saqlab
# qoladi demak bufferlanmagan holatini true qilib qo'yish buffer bo'lmaganini anglatadi shunda buffer o'chirilgan hisoblanadi
ENV PYTHONDONTWRITEBYTECODE 1
# PYTHONDONTWRITEBYTECODE degani fayllarni Bayt kod (.pyc) farmatga o'tkazishi to'xtatiladi va Python (.pyc) fayllarni yaratmaydi.
# bu nima narsalarga foyda bo'lishi mumkin ochiladigan kontainer da vaqtinchalik bo'lgan ortiqcha fayllarni saqlamaydi : bu degani kontainer toza saqlanadi

WORKDIR /app
# container ochilganda qayerda saqlashini ko'rsatadi
COPY requirements.txt requirements.txt
# shu fayldan kutubxonalarni oladi
RUN pip install -r requirements.txt

CMD ["bash", "-c", "python manage.py runserver 0.0.0.0:8080 "]

# va yoziladigan kamandalar run kodi bilan ishga tushiriladi bu narsaga istalgan terminal kodini kiritas bo'oladi
# container ishga tushgan vaqtda bu kamandalarni o'zining muhitida ishga tushiradi
COPY . .
# COPT . . bu narsa shu yozilgan barcha kodlarni xotiraga saqlab qolib keyingi ishga tushirilgan vatqida boshidan
# bo'lmasdan shu saqlab qolgan malumotlarini ishga tushiradi agar o'zgarish bo'lsa uni davom etriadi
