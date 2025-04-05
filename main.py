import random 
import discord
from discord.ext import commands
import time


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = "&", intents = intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def matematica(ctx):
    preguntas_mates = [
        ("¿Cuánto es 5 + 3?", "8"),
        ("¿Cuál es la raíz cuadrada de 16?", "4"),
        ("¿Cuánto es 12 x 6?", "72"),
        ("Si tienes un ángulo de 90°, ¿cómo se llama?", "Recto"),
        ("¿Cuánto es 2³?", "8")
    ]

    pregunta, respuesta_correcta = random.choice(preguntas_mates)

    await ctx.send(f"Pregunta de Mates {pregunta}")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    mensaje = await bot.wait_for("message", check=check)

    if mensaje.content.strip().lower() == respuesta_correcta.lower():
        await ctx.send("Correcto!")
    else:
        await ctx.send(f"nop, la respuesta era: {respuesta_correcta}")

@bot.command()
async def comunicacion(ctx):
    preguntas_comu = [
        ("que tipo de palabra es rapidamente?", "adverbio"),
        ("cual es el sinonimo de efimero?", "fugaz"),
        ("cual es el sujeto de la oracion: el perro de juan ladra fuerte?", "el perro"),
        ("que significa la palabra: sagaz?", "inteligente"),
        ("quee figura literiaria se usa en El viento susurraba en la noche??", "personificacion")

    ]

    pregunta, respuesta_correcta = random.choice(preguntas_comu)
    
    await ctx.send(f"la pregunta es {pregunta}")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    mensaje = await bot.wait_for('message', check=check)
    
    if mensaje.content.strip().lower() == respuesta_correcta.lower():
        await ctx.send ("correcto!!")
    else:
        await ctx.send (f"nop, la respuesta era {respuesta_correcta}")

@bot.command()
async def ingles(ctx):
    preguntas_ingles = [
        ("como se dice perro en ingles?", "dog"),
        ("como se traduce la palabra 'table'?", "mesa"),
        ("cual es el pasado de 'go'?", "went"),
        ("que significa 'blue' en español?", "azul"),
        ("como se dice 'grande' en ingles?", "big")
        ]

    pregunta, respuesta_correcta = random.choice(preguntas_ingles)

    await ctx.send(f"la pregunta es {pregunta}")
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    mensaje = await bot.wait_for('message', check=check)

    if mensaje.content.strip().lower() == respuesta_correcta.lower():
        await ctx.send("correcto!!")
    else:
        await ctx.send(f"nop, la respuesta era {respuesta_correcta}")


@bot.command()
async def ciencias_sociales(ctx):
    preguntas_sociales = [
        ("quien descubrio america?", "cristobal colon"),
        ("en que año comenzo la revolucion francesa?", "1789"),
        ("cual fue la primera civilizacion en america?", "olmeca"),
        ("cual es la capital de egipto?", "el cairo"),
        ("quien escribio la declaracion de independencia de eeuu?", "thomas jefferson")
    ]

    pregunta, respuesta_correcta = random.choice(preguntas_sociales)

    await ctx.send(f"la pregunta es {pregunta}")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    mensaje = await bot.wait_for('message', check=check)

    if mensaje.content.strip().lower() == respuesta_correcta.lower():
        await ctx.send("correcto!!")
    else:
        await ctx.send(f"nop, la respuesta era {respuesta_correcta}")


@bot.command()
async def ciencia_tecnologia(ctx):
    preguntas_ciencia = [
        ("que gas necesitamos para respirar?", "oxigeno"),
        ("cual es el planeta mas grande del sistema solar?", "jupiter"),
        ("quien descubrio la ley de la gravedad?", "isaac newton"),
        ("que tipo de energia usa un panel solar?", "solar"),
        ("que elemento tiene el simbolo 'H' en la tabla periodica?", "hidrogeno")
    ]

    pregunta, respuesta_correcta = random.choice(preguntas_ciencia)

    await ctx.send(f"la pregunta es {pregunta}")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    mensaje = await bot.wait_for('message', check=check)

    if mensaje.content.strip().lower() == respuesta_correcta.lower():
        await ctx.send("correcto!!")
    else:
        await ctx.send(f"nop, la respuesta era {respuesta_correcta}")

@bot.command()
async def arte_cultura(ctx):
    preguntas_arte = [
        ("quien pinto la mona lisa?", "leonardo da vinci"),
        ("cual es el genero musical tipico de argentina?", "tango"),
        ("cual es el teatro mas famoso de londres?", "globe"),
        ("quien escribio romeo y julieta?", "william shakespeare"),
        ("cual es el instrumento musical nacional de peru?", "charango")
    ]

    pregunta, respuesta_correcta = random.choice(preguntas_arte)

    await ctx.send(f"la pregunta es {pregunta}")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    mensaje = await bot.wait_for('message', check=check)

    if mensaje.content.strip().lower() == respuesta_correcta.lower():
        await ctx.send("correcto!!")
    else:
        await ctx.send(f"nop, la respuesta era {respuesta_correcta}")

@bot.command()
async def dpcc(ctx):
    preguntas_dpcc = [
        ("que es la empatia?", "ponerse en el lugar del otro"),
        ("que significa el derecho a la igualdad?", "todos somos iguales ante la ley"),
        ("que es el bullying?", "acoso escolar"),
        ("cual es la importancia del respeto?", "convivencia armoniosa"),
        ("que significa ser ciudadano?", "tener derechos y deberes")
    ]

    pregunta, respuesta_correcta = random.choice(preguntas_dpcc)

    await ctx.send(f"la pregunta es {pregunta}")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    mensaje = await bot.wait_for('message', check=check)

    if mensaje.content.strip().lower() == respuesta_correcta.lower():
        await ctx.send("correcto!!")
    else:
        await ctx.send(f"nop, la respuesta era {respuesta_correcta}")

@bot.command()
async def etp(ctx):
    preguntas_etp = [
        ("que es un emprendimiento?", "iniciar un negocio"),
        ("que significa 'pymes'?", "pequeñas y medianas empresas"),
        ("que es la contabilidad?", "registro de transacciones economicas"),
        ("cual es el objetivo de un curriculum vitae?", "presentar experiencia laboral"),
        ("que es el marketing?", "estrategia para vender productos o servicios")
    ]

    pregunta, respuesta_correcta = random.choice(preguntas_etp)

    await ctx.send(f"la pregunta es {pregunta}")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    mensaje = await bot.wait_for('message', check=check)

    if mensaje.content.strip().lower() == respuesta_correcta.lower():
        await ctx.send("correcto!!")
    else:
        await ctx.send(f"nop, la respuesta era {respuesta_correcta}")

bot.run("MTM1NTg3NjYwMDI5NzY4NTA2Mg.GDflL_.5XbahoycnWJhFJRka7w9isyENQ6fZIYt-4wd8oWAZA")
