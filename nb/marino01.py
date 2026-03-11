import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _(os):
    os.environ["GOOGLE_API_KEY"] = "your_key_here"

    return


@app.cell
def _():
    from google import genai
    import os

    try:
        print(
            genai.Client(api_key=os.environ["GOOGLE_API_KEY"])
            .models.generate_content(
                model="gemini-2.5-flash", contents="Say hi in one sentence."
            )
            .text
        )
    except RuntimeError as e:
        print(f"Ops...{e}")
    return (os,)


if __name__ == "__main__":
    app.run()
