"""Pure logic with no Discord dependency (except embeds): easy to unit test.

Rule of thumb used throughout the project: keep the *decisions* here and the
*Discord plumbing* in cogs. A cog command should mostly be "parse input, call a
core function, format the result".
"""
