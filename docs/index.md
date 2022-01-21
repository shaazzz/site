# مقدمات

برای اطلاعات بیشتر به
[mkdocs.org](https://www.mkdocs.org)
سر بزنید.

## موارد

!!! warning "نکته"
    راهنما در حال تکمیل است.

## دکمه

[:fontawesome-brands-telegram: در گروه تلگرامی شاززز عضو شوید](https://t.me/shaazzz_group){ .md-button .md-button--primary}

## کد

``` cpp title="انتخاب \(r\) از \(n\)"
ll C(ll n, ll r) {
    if (r < 0 || n < r)
        return 0;
    return fact[n] * inv[r] % MOD * inv[n-r] % MOD;
}
```

## جدول

| نوع امتحان |‌‌ تعداد سوالات | زمان برای هر سوال |
|:----:|:----:|:---:|
| مرحله اول | ۲۰ سوال | ۶ دقیقه |
| مرحله دوم | ۱۵ سوال | ۱۰ دقیقه |

## فرمتینگ

==هایلایت==
برای مهم تر نشون دادن چیزی

برای باز کردن صدا توی زوم
++alt+f4++

## تصویر

<figure markdown>
  ![Image title](https://dummyimage.com/600x400/)
  <figcaption>Image caption</figcaption>
</figure>

## لیست

- [x] آماده کردن `mkdocs`
- [ ] نوشتن توضیحات اولیه

## لاتک

\[ \sum_{i=0}^{n}{2^i} = 2^{n-1} \]

## صفحه‌های دیگه

- [المپیاد کامپیوتر ۱۰۱](intro/index.md)