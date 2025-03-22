import discord
from discord.ext import commands
import asyncio
from trivia import obtener_pregunta_aleatoria

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("¡Comando no encontrado! Usa `$ayuda` para ver la lista de comandos disponibles.")

@bot.command()
async def hola(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')
    
@bot.command()
async def ayuda(ctx):
    """Muestra una lista de comandos disponibles y su descripción."""
    embed = discord.Embed(
        title="Comandos Disponibles",
        description="Estos son los comandos que puedes utilizar:",
        color=0x1ABC9C
    )
    embed.add_field(name="$hola", value="Saluda al bot.", inline=False)
    embed.add_field(name="$ayuda", value="Muestra este mensaje de ayuda.", inline=False)
    embed.add_field(name="$masinfo", value="Muestra enlaces para obtener mas información.", inline=False)
    embed.add_field(name="$inundaciones", value="Muestra información sobre inundaciones relacionadas al cambio climático.", inline=False)
    embed.add_field(name="$tornados", value="Muestra información sobre tornados extremos.", inline=False)
    embed.add_field(name="$sequias", value="Muestra información sobre sequías prolongadas.", inline=False)
    embed.add_field(name="$catastrofes", value="Muestra información sobre catástrofes climáticas.", inline=False)
    embed.add_field(name="$trivia", value="Inicia un sencillo juego de trivia sobre cambio climático.", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def masinfo(ctx):
    """Muestra enlaces para obtener más información sobre el cambio climático."""
    embed = discord.Embed(
        title="Más Información sobre el Cambio Climático",
        description="Consulta los siguientes enlaces para obtener más detalles:",
        color=0x1ABC9C
    )
    embed.add_field(name="Climate Crisis: Race We Can Win", value="https://www.un.org/es/un75/climate-crisis-race-we-can-win", inline=False)
    embed.add_field(name="Causas y Efectos del Cambio Climático", value="https://www.un.org/es/climatechange/science/causes-effects-climate-change", inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def inundaciones(ctx):
    """Muestra información sobre inundaciones relacionadas al cambio climático."""
    embed = discord.Embed(
        title="Inundaciones",
        description="Las inundaciones, provocadas por lluvias intensas y el aumento del nivel del mar, son un efecto evidente del cambio climático. Descubre más detalles en la fuente indicada.",
        color=0x3498DB
    )
    embed.set_image(url="https://www.salyroca.es/asset/thumbnail,992,558,center,center/media/salyroca/images/2021/08/10/2021081012135060624.jpg")
    embed.add_field(name="Fuente", value="https://www.un.org/es/climatechange/science/causes-effects-climate-change", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def tornados(ctx):
    """Muestra información sobre tornados extremos."""
    embed = discord.Embed(
        title="Tornados",
        description="Los tornados pueden intensificarse y arrasar con aldeas, siendo un claro indicador de los extremos climáticos generados por el cambio climático. Consulta la fuente para más información.",
        color=0xE74C3C
    )
    embed.set_image(url="https://planetamaunaloa.com/wp-content/uploads/2021/12/nikolas-noonan-n_3kdpSkrJo-unsplash-1024x683.jpg")
    embed.add_field(name="Fuente", value="https://www.un.org/es/un75/climate-crisis-race-we-can-win", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def sequias(ctx):
    """Muestra información sobre sequías prolongadas."""
    embed = discord.Embed(
        title="Sequías",
        description="Las sequías, o periodos prolongados de escasez de agua, se han vuelto más comunes y severas por el cambio climático. Más detalles en la fuente.",
        color=0xF1C40F
    )
    embed.set_image(url="https://images.fineartamerica.com/images/artworkimages/mediumlarge/3/1-poor-asian-children-are-holding-green-vegetables-in-dry-cracked-somchai-sanvongchaiya.jpg")
    embed.add_field(name="Fuente", value="https://www.un.org/es/climatechange/science/causes-effects-climate-change", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def catastrofes(ctx):
    """Muestra información sobre catástrofes climáticas."""
    embed = discord.Embed(
        title="Catástrofes Climáticas",
        description="El cambio climático puede desencadenar catástrofes como incendios forestales, tormentas extremas y huracanes que afectan a comunidades enteras. Lee más en la fuente recomendada.",
        color=0x9B59B6
    )
    embed.set_image(url="https://saberdetodo.com/wp-content/uploads/tipos-de-desastres-naturales-1-1-e1599131192123.jpg")
    embed.add_field(name="Fuente", value="https://www.un.org/es/un75/climate-crisis-race-we-can-win", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def trivia(ctx):
    """Inicia un sencillo juego de trivia sobre cambio climático."""
    pregunta_actual = obtener_pregunta_aleatoria()
    
    mensaje_pregunta = f"Pregunta: {pregunta_actual['pregunta']}\n"
    for opcion in pregunta_actual['opciones']:
        mensaje_pregunta += f"{opcion}\n"
    mensaje_pregunta += "\nResponde con A, B, C o D."
    
    await ctx.send(mensaje_pregunta)
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content.upper() in ["A", "B", "C", "D"]
    
    try:
        msg = await bot.wait_for('message', timeout=10.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send(f"¡Tiempo agotado! La respuesta correcta era {pregunta_actual['respuesta']}: {pregunta_actual['explicacion']}")
        return
    
    if msg.content.upper() == pregunta_actual['respuesta']:
        await ctx.send(f"¡Correcto! {pregunta_actual['explicacion']}")
    else:
        await ctx.send(f"Incorrecto. La respuesta correcta era {pregunta_actual['respuesta']}: {pregunta_actual['explicacion']}")

bot.run("MTI4NDMxNDE5NzU0MjU2ODAxNw.GRPf8E.4RDkdVZIkKApgiN1qMXhRUOt7KlBx4h8vWMvXU")