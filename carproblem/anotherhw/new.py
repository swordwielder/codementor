def main():
    # This is the size of the window; feel free to tweak it. However,
    # please don’t make this gigantic (about 800x800 should be max),
    # since your TA may not have a screen with crazy-large resolution.
    wid = 400
    hei = 600
    # This creates the Game object. The first param is the window name;
    # the second is the framerate you want (20 frames per second, in this
    # example); the last two are the window / game space size.
    game = Game("Three Shapes", 20, wid,hei)
    # This affects how the distance calculation in the "nearby" calls
    # works; the default is to measure center-to-center. But if anybody
    # wants to measure edge-to-edge, they can turn on this feature.
    # game.config_set("account_for_radii_in_dist", True)
    # You get to decide what spawn() does. This sets up the initial
    # objects that you want to create, at the beginning of the game (if
    # any). Of course, you can remove this is you want to create objects
    # some other way.
    spawn(game, wid,hei)
    # game loop. Runs forever, unless the game ends.
    while not game.is_over():
    game.do_nearby_calls()
    game.do_move_calls()
    game.do_edge_calls()
    game.draw()
    # You get to decide what spawn_more() does (if anything). This
    # allows you to spawn additional objects over time. It is
    # called once per game tick.
    spawn_more(game, wid,hei)