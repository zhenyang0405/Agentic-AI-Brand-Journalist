def draft_pitch_email(blog_title: str, blog_post_draft: str, target_audience: str) -> str:
    """
    Drafts a pitch email for a blog post.

    Args:
        blog_title (str): The title of the blog post.
        blog_post_draft: The full text of the blog post draft.
        target_audience: The audience the post is intended for.

    Returns:
        A formatted pitch email as a string.
    """
    # A simple template for the email
    email_template = f"""
    **Subject: New Blog Post Proposal: {blog_title}**

    Hi Team,

    I have drafted a new blog post for our blog.

    **Topic:** Based on the content, this post is about [AI to generate topic].
    **Target Audience:** {target_audience}

    **Draft:**
    ---
    {blog_post_draft}...
    ---

    Please review and let me know if this is ready for publishing.

    Best,
    Autonomous Brand Journalist
    """
    return email_template