""" def before_all(context, feature):
    context.db.create() """

""" def after_step(context, step):
    if step.status == "failed":
        import ipdb
        ipdb.post_mortem(step.exc_traceback) """