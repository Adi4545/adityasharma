#!/usr/bin/env python3
"""
Build one comprehensive Transformer teaching PDF (Parts 0–20).
Based on Vaswani et al., 2017 — Attention Is All You Need.

Teaching style for every concept:
  problem → simple language → toy numerical example → math with shapes
  → computation → where it fits → what fails if removed → paper connection
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    Preformatted, KeepTogether, HRFlowable,
)
import shutil
import os

OUT_ARTIFACT = "/opt/cursor/artifacts/Transformer_Complete_Course_Attention_Is_All_You_Need.pdf"
OUT_WORKSPACE = "/workspace/transformer-course/Transformer_Complete_Course_Attention_Is_All_You_Need.pdf"

NAVY = HexColor("#0F172A")
BLUE = HexColor("#1E3A5F")
ACCENT = HexColor("#1D4ED8")
GRAY = HexColor("#334155")
LIGHT = HexColor("#F1F5F9")
RULE = HexColor("#CBD5E1")
CODE_BG = HexColor("#F8FAFC")
GREEN = HexColor("#065F46")
WARN = HexColor("#9A3412")


def styles():
    s = getSampleStyleSheet()
    s.add(ParagraphStyle(
        "CoverTitle", parent=s["Title"], fontName="Helvetica-Bold",
        fontSize=26, leading=32, textColor=NAVY, alignment=TA_CENTER, spaceAfter=12
    ))
    s.add(ParagraphStyle(
        "CoverSub", parent=s["Normal"], fontName="Helvetica",
        fontSize=12, leading=16, textColor=GRAY, alignment=TA_CENTER, spaceAfter=6
    ))
    s.add(ParagraphStyle(
        "PartTitle", parent=s["Heading1"], fontName="Helvetica-Bold",
        fontSize=16, leading=20, textColor=NAVY, spaceBefore=4, spaceAfter=10
    ))
    s.add(ParagraphStyle(
        "CourseH2", parent=s["Heading2"], fontName="Helvetica-Bold",
        fontSize=12.5, leading=16, textColor=BLUE, spaceBefore=12, spaceAfter=6
    ))
    s.add(ParagraphStyle(
        "CourseH3", parent=s["Heading3"], fontName="Helvetica-Bold",
        fontSize=11, leading=14, textColor=HexColor("#1E40AF"), spaceBefore=9, spaceAfter=4
    ))
    s.add(ParagraphStyle(
        "CourseBody", parent=s["Normal"], fontName="Helvetica",
        fontSize=9.5, leading=13, textColor=NAVY, alignment=TA_JUSTIFY, spaceAfter=7
    ))
    s.add(ParagraphStyle(
        "CourseBullet", parent=s["Normal"], fontName="Helvetica",
        fontSize=9.5, leading=12.5, textColor=NAVY, leftIndent=14, spaceAfter=2
    ))
    s.add(ParagraphStyle(
        "CourseCallout", parent=s["Normal"], fontName="Helvetica-Oblique",
        fontSize=9.5, leading=12.5, textColor=ACCENT, leftIndent=8, rightIndent=8,
        spaceBefore=4, spaceAfter=8, borderPadding=4
    ))
    s.add(ParagraphStyle(
        "CourseWarn", parent=s["Normal"], fontName="Helvetica-Oblique",
        fontSize=9.5, leading=12.5, textColor=WARN, leftIndent=8, rightIndent=8,
        spaceBefore=4, spaceAfter=8
    ))
    s.add(ParagraphStyle(
        "CourseKey", parent=s["Normal"], fontName="Helvetica-Bold",
        fontSize=9.5, leading=12.5, textColor=GREEN, leftIndent=8, rightIndent=8,
        spaceBefore=4, spaceAfter=8
    ))
    s.add(ParagraphStyle(
        "CourseMono", parent=s["Code"], fontName="Courier",
        fontSize=7.6, leading=9.6, textColor=NAVY, backColor=CODE_BG,
        leftIndent=3, rightIndent=3, spaceBefore=3, spaceAfter=7
    ))
    s.add(ParagraphStyle(
        "CourseEq", parent=s["Normal"], fontName="Courier-Bold",
        fontSize=9, leading=12, textColor=NAVY, alignment=TA_CENTER,
        spaceBefore=6, spaceAfter=6
    ))
    s.add(ParagraphStyle(
        "CourseCaption", parent=s["Normal"], fontName="Helvetica-Oblique",
        fontSize=8.5, leading=11, textColor=GRAY, alignment=TA_CENTER, spaceAfter=8
    ))
    s.add(ParagraphStyle(
        "CourseTOC", parent=s["Normal"], fontName="Helvetica",
        fontSize=10, leading=14, textColor=NAVY, leftIndent=10, spaceAfter=3
    ))
    s.add(ParagraphStyle(
        "CourseFooter", parent=s["Normal"], fontName="Helvetica",
        fontSize=8, textColor=GRAY, alignment=TA_CENTER
    ))
    return s


def hr():
    return HRFlowable(width="100%", thickness=0.7, color=RULE, spaceBefore=4, spaceAfter=8)


def P(text, style):
    return Paragraph(text, style)


def bullets(items, st):
    return [P(f"• {x}", st["CourseBullet"]) for x in items]


def mono(text, st):
    return Preformatted(text.rstrip("\n"), st["CourseMono"])


def add_header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(GRAY)
    canvas.drawString(0.75 * inch, 0.45 * inch, "Transformer Complete Course — Attention Is All You Need (2017)")
    canvas.drawRightString(letter[0] - 0.75 * inch, 0.45 * inch, f"Page {doc.page}")
    canvas.restoreState()


def simple_table(rows, col_widths, st):
    data = []
    for r in rows:
        data.append([P(c, st["CourseBullet"]) for c in r])
    t = Table(data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), LIGHT),
        ("GRID", (0, 0), (-1, -1), 0.4, RULE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return t


def build():
    st = styles()
    story = []

    # =====================================================================
    # COVER
    # =====================================================================
    story.append(Spacer(1, 1.0 * inch))
    story.append(P("Attention Is All You Need", st["CoverTitle"]))
    story.append(P("A First-Principles Complete Course", st["CoverTitle"]))
    story.append(Spacer(1, 0.15 * inch))
    story.append(P("From absolute beginner → full understanding, explanation,", st["CoverSub"]))
    story.append(P("mental simulation, and miniature PyTorch implementation", st["CoverSub"]))
    story.append(Spacer(1, 0.2 * inch))
    story.append(hr())
    story.append(P("Based on Vaswani et al., 2017 (arXiv:1706.03762)", st["CoverSub"]))
    story.append(P("Parts 0–20 · Intuition → Mathematics → Computation → Architecture", st["CoverSub"]))
    story.append(Spacer(1, 0.25 * inch))
    story.append(P(
        "Teaching rule: for every component we ask — What problem does this solve? "
        "What happens to the tensor? Why is this operation necessary? "
        "What fails if we remove it? Where does the paper state it?",
        st["CourseCallout"]
    ))
    story.append(Spacer(1, 0.3 * inch))
    story.append(P("Running examples throughout:", st["CoverSub"]))
    story.append(P("<b>English → French</b>: “I love cats” → “J’aime les chats”", st["CoverSub"]))
    story.append(P("Pronoun: “The animal didn’t cross the road because it was tired.”", st["CoverSub"]))
    story.append(Spacer(1, 0.35 * inch))
    story.append(P(
        "Architecture note: this course reconstructs the <b>original 2017 Post-LN</b> Transformer "
        "and explicitly contrasts it with modern Pre-LN variants.",
        st["CourseKey"]
    ))
    story.append(PageBreak())

    # =====================================================================
    # TOC
    # =====================================================================
    story.append(P("Table of Contents", st["PartTitle"]))
    story.append(hr())
    toc = [
        "Part 0 — How to Read This Paper",
        "Part 1 — Minimum Prerequisites (the vital 20%)",
        "Part 2 — Why Attention Was Needed",
        "Part 3 — Attention From Zero (full numerical walkthrough)",
        "Part 4 — Self-Attention (contextualization + cost)",
        "Part 5 — Multi-Head Attention (subspaces + shapes)",
        "Part 6 — Positional Encoding (order without recurrence)",
        "Part 7 — The Feed-Forward Network",
        "Part 8 — Residual Connections + Layer Normalization (Post-LN vs Pre-LN)",
        "Part 9 — Build the Encoder From Scratch",
        "Part 10 — The Decoder (masking + cross-attention)",
        "Part 11 — Complete Transformer Data Flow",
        "Part 12 — Training the Transformer",
        "Part 13 — Inference / Generation",
        "Part 14 — The Paper’s Equations (decoded)",
        "Part 15 — Original 2017 Architecture Specs",
        "Part 16 — Complexity and Why Transformers Scale",
        "Part 17 — Reading the Results Section",
        "Part 18 — Limitations of the Original Transformer",
        "Part 19 — Implement a Miniature Transformer (PyTorch)",
        "Part 20 — Final Master Understanding (quiz + answer key)",
    ]
    for t in toc:
        story.append(P(t, st["CourseTOC"]))
    story.append(Spacer(1, 10))
    story.append(P(
        "This PDF is self-contained. Read in order. Do not skip numerical examples — "
        "they are where understanding becomes real. Parts 3, 4, 5, 6, 10, 11, 12, and 19 "
        "are intentionally the densest.",
        st["CourseKey"]
    ))
    story.append(PageBreak())

    # =====================================================================
    # PART 0
    # =====================================================================
    story.append(P("PART 0 — How to Read This Paper", st["PartTitle"]))
    story.append(hr())

    story.append(P("0.1 What is a research paper?", st["CourseH2"]))
    story.append(P(
        "A research paper is a compressed scientific argument. It is not a textbook and not a blog tutorial. "
        "Authors write for other researchers who already share vocabulary, notation, and prior results. "
        "That is why a first encounter with “Attention Is All You Need” feels dense: many sentences "
        "assume you already know seq2seq, attention, and BLEU.",
        st["CourseBody"]
    ))
    story.append(P("Almost every ML paper has this skeleton:", st["CourseBody"]))
    story.extend(bullets([
        "<b>Problem:</b> something is limited, expensive, inaccurate, or hard to scale",
        "<b>Idea:</b> a new method, architecture, training procedure, or theory",
        "<b>Method:</b> precise definition of the model and how it is trained",
        "<b>Evidence:</b> experiments showing it works (often better than baselines)",
        "<b>Limits:</b> what remains unsolved (sometimes understated)",
    ], st))
    story.append(P(
        "Your first goal is not to understand every sentence. Your first goal is to extract: "
        "problem → idea → method → evidence.",
        st["CourseKey"]
    ))

    story.append(P("0.2 How to read a machine-learning paper (multiple passes)", st["CourseH2"]))
    story.append(P(
        "Professionals almost never read linearly once. Use passes with different jobs.",
        st["CourseBody"]
    ))
    story.extend(bullets([
        "<b>Pass 1 — Map:</b> title, abstract, first page of intro, all figures, conclusion. "
        "What claim? What is Figure 1? What datasets?",
        "<b>Pass 2 — Architecture:</b> read §3 while staring at Figure 1. Trace input → process → output.",
        "<b>Pass 3 — Equations:</b> for each equation list symbols, shapes, and the actual computation. "
        "Recompute with tiny numbers.",
        "<b>Pass 4 — Experiments:</b> datasets, metrics, baselines, ablations, training cost.",
        "<b>Pass 5 — Limitations:</b> what they did not solve; what assumptions remain; what later work changed.",
    ], st))
    story.append(P(
        "Common mistake: treating every sentence as equally important. "
        "Better habit: classify each paragraph as motivation / architecture / equation / experiment / claim.",
        st["CourseWarn"]
    ))

    story.append(P("0.3 What problem are the authors solving?", st["CourseH2"]))
    story.append(P(
        "In 2017, strong sequence models (especially machine translation) relied on recurrence (RNNs/LSTMs) "
        "and sometimes convolutions. Recurrence processes tokens one-by-one: hidden state h_t waits for h_{t−1}. "
        "That sequential dependence makes training hard to parallelize across time and makes long-range "
        "dependencies travel through many steps.",
        st["CourseBody"]
    ))
    story.append(P(
        "Core research question: <i>Can we build a strong sequence transduction model that relies entirely on "
        "attention — with no recurrence and no convolution?</i> Their answer is the Transformer.",
        st["CourseCallout"]
    ))

    story.append(P("0.4 What “contribution” means", st["CourseH2"]))
    story.append(P(
        "A contribution is the new reusable thing given to the field. For this paper: an encoder–decoder "
        "architecture based solely on attention (self-attention + multi-head attention + cross-attention), "
        "with strong translation quality and better training parallelization than recurrent models.",
        st["CourseBody"]
    ))
    story.append(P(
        "Later models (BERT, GPT, ViT, LLaMA, …) are <b>impact</b> — not this paper’s claimed 2017 contribution. "
        "Stay loyal to 2017 when reconstructing the architecture (Post-LN, sinusoidal PE, encoder–decoder MT).",
        st["CourseWarn"]
    ))

    story.append(P("0.5 Distinguishing paper pieces", st["CourseH2"]))
    story.append(simple_table([
        ["<b>Piece</b>", "<b>Answers</b>", "<b>Where in paper</b>"],
        ["Motivation", "Why it matters", "§1 Introduction"],
        ["Architecture", "What the model is", "§3 Model + Fig. 1"],
        ["Equations", "Exact computation", "§3.2–3.5"],
        ["Training", "How optimized", "§5 Training"],
        ["Results", "Did it work?", "§6 Results (BLEU)"],
        ["Ablations", "What parts matter?", "§5.3 / tables"],
        ["Limitations", "Still unsolved", "implied + later work"],
    ], [1.3*inch, 2.3*inch, 2.8*inch], st))

    story.append(P("0.6 Mental map of the paper", st["CourseH2"]))
    story.append(mono("""
[PROBLEM] Recurrent MT is sequential → hard parallelization, hard long-range deps
[IDEA]    Attention only → Transformer encoder–decoder
[CORE]    Scaled Dot-Product Attention → Multi-Head → Self / Cross / Masked
[SUPPORT] Embeddings + Positional Encoding; FFN; Add & Norm (Post-LN); N=6 stacks
[TRAIN]   Teacher forcing, cross-entropy, Adam+schedule, dropout, label smoothing
[EVIDENCE] WMT BLEU, speed/params, ablations
[GOAL]    Mentally simulate tokens → probabilities and explain WHY each piece exists
""", st))

    story.append(P("0.7 Three buckets you must never mix", st["CourseH2"]))
    story.extend(bullets([
        "<b>Architecture:</b> what tensors exist and how they transform (Fig. 1, equations).",
        "<b>Training procedure:</b> loss, optimizer, schedule, teacher forcing, label smoothing.",
        "<b>Implementation details:</b> dropout rates, batching tricks, beam search hyperparameters.",
    ], st))
    story.append(P(
        "Separate forever: architecture vs training procedure vs implementation details.",
        st["CourseKey"]
    ))

    story.append(P("0.8 How this course maps onto the paper", st["CourseH2"]))
    story.extend(bullets([
        "Parts 1–2 build prerequisites and historical motivation (§1–2).",
        "Parts 3–8 unpack every block inside Fig. 1 (§3.2–3.5).",
        "Parts 9–11 assemble encoder, decoder, and full dataflow (§3.1).",
        "Parts 12–13 cover training and inference (§5).",
        "Parts 14–17 decode equations, specs, complexity, and results (§4–6).",
        "Parts 18–20 limitations, code, and mastery check.",
    ], st))
    story.append(PageBreak())

    # =====================================================================
    # PART 1
    # =====================================================================
    story.append(P("PART 1 — Minimum Prerequisites (Only the Vital 20%)", st["PartTitle"]))
    story.append(hr())
    story.append(P(
        "We will not dump an entire deep-learning course. These are the concepts you need for 80–90% of the paper. "
        "If a later part mentions a shape you do not understand, return here.",
        st["CourseCallout"]
    ))

    story.append(P("1.1 Vectors", st["CourseH2"]))
    story.append(P(
        "A vector is an ordered list of numbers. In Transformers, almost everything is a vector: a token embedding, "
        "a query, a key, a value, an attention output, an FFN hidden state.",
        st["CourseBody"]
    ))
    story.append(mono("v = [1.0, 0.5, -0.2]     # shape: (3,)   a 3-dimensional vector", st))
    story.append(P(
        "Intuition: each dimension is one learned feature axis. You do not need to interpret each axis by hand. "
        "What matters is geometry: directions, lengths, and angles between vectors.",
        st["CourseBody"]
    ))

    story.append(P("1.2 Matrices and shapes", st["CourseH2"]))
    story.append(P(
        "A matrix is a rectangle of numbers: rows × columns. Notation: X ∈ R^(T × d) means X has T rows and d columns, "
        "with real numbers. In this course, <b>one row = one token’s representation</b>.",
        st["CourseBody"]
    ))
    story.append(mono("""
X ∈ R^(T × d)
  T = sequence length (number of tokens)
  d = model dimension (size of each token vector)
  one ROW  = one token's representation
  one COL  = one feature across all tokens

Example: 3 tokens ("I","love","cats"), d=4
X = [[ 0.1, 0.2, 0.0, 0.4],   # "I"
     [ 0.5, 0.1, 0.3, 0.0],   # "love"
     [-0.2, 0.6, 0.1, 0.2]]   # "cats"
shape(X) = (3, 4)
""", st))

    story.append(P("1.3 Matrix multiplication", st["CourseH2"]))
    story.append(P(
        "If A is (m × n) and B is (n × p), then AB is (m × p). The inner dimensions must match (both n). "
        "Each entry C[i,j] is the dot product of row i of A with column j of B.",
        st["CourseBody"]
    ))
    story.append(mono("""
A (2×3) @ B (3×2) → C (2×2)

Why Transformers care: multiplying by a weight matrix W is how we linearly transform vectors
(e.g., turn embeddings into Queries / Keys / Values, or project to vocabulary logits).

Shape drill:
  X (T×d) @ W (d×d_k) → (T×d_k)     # project every token
  Q (T×d_k) @ Kᵀ (d_k×T) → (T×T)    # all-pairs scores
""", st))

    story.append(P("1.4 Dot products as similarity", st["CourseH2"]))
    story.append(P(
        "The dot product of two equal-length vectors is the sum of elementwise products. "
        "Large positive ≈ similar direction; near zero ≈ unrelated; negative ≈ opposite.",
        st["CourseBody"]
    ))
    story.append(mono("""
q = [1, 2, 0]
k = [1, 0, 3]
q·k = 1*1 + 2*0 + 0*3 = 1

In attention, score(query, key) starts as a dot product:
"how well does this query match this key?"
""", st))

    story.append(P("1.5 Softmax and probability", st["CourseH2"]))
    story.append(P(
        "Softmax turns a list of real scores into a probability distribution: all values positive and sum to 1.",
        st["CourseBody"]
    ))
    story.append(P("softmax(z)_i = exp(z_i) / Σ_j exp(z_j)", st["CourseEq"]))
    story.append(mono("""
scores = [2.0, 1.0, 0.1]
exp    = [7.389, 2.718, 1.105]
sum    = 11.212
probs  = [0.659, 0.242, 0.099]   # attention weights / next-token probs
""", st))
    story.append(P(
        "In attention, softmax tells each token: “how much weight should I give each other token?” "
        "In the final layer, softmax over vocabulary tells: “how likely is each next word?”",
        st["CourseKey"]
    ))

    story.append(P("1.6 Neural networks (minimum)", st["CourseH2"]))
    story.append(P(
        "A neural network layer is usually: linear transform → nonlinearity → (maybe) another linear transform. "
        "Learned parameters (weights/biases) are adjusted by gradient descent so predictions improve.",
        st["CourseBody"]
    ))
    story.append(mono("y = activation(x W + b)     # e.g., ReLU = max(0, ·)", st))

    story.append(P("1.7 Embeddings", st["CourseH2"]))
    story.append(P(
        "Computers do not understand words. An embedding table maps each token ID to a learned vector of size d_model. "
        "Similar words often end up with similar vectors after training — but embeddings alone are not contextual. "
        "“Bank” in “river bank” and “bank account” start with the same embedding until context is mixed in by attention.",
        st["CourseBody"]
    ))
    story.append(mono("""
vocab: {"I":0, "love":1, "cats":2, "<BOS>":3, "J'aime":4, "les":5, "chats":6, "<EOS>":7}
ids:   [0, 1, 2]
E = EmbeddingLookup(ids)   # shape (3, d_model)
""", st))

    story.append(P("1.8 Sequence-to-sequence + encoder–decoder", st["CourseH2"]))
    story.append(P(
        "Sequence-to-sequence (seq2seq) means: input sequence → output sequence of possibly different length "
        "(translation, summarization). Classic pattern:",
        st["CourseBody"]
    ))
    story.append(mono("""
ENCODER: read source sentence, build contextual representations (memory)
DECODER: generate target sentence token by token, using encoder memory

Example:
  source: I love cats
  target: J'aime les chats
""", st))

    story.append(P("1.9 RNNs/LSTMs at conceptual level", st["CourseH2"]))
    story.append(P(
        "An RNN reads tokens left-to-right, updating a hidden state. LSTMs improve memory of longer signals, "
        "but the core constraint remains: step t waits for step t−1. That sequential dependence is the bottleneck "
        "the Transformer attacks.",
        st["CourseBody"]
    ))
    story.append(mono("""
RNN:
  h1 = f(x1, h0)
  h2 = f(x2, h1)   # must wait for h1
  h3 = f(x3, h2)   # must wait for h2
Cannot fully parallelize across time on a GPU.
""", st))

    story.append(P("1.10 Loss, gradients, and “learning”", st["CourseH2"]))
    story.append(P(
        "Training compares the model’s predicted token probabilities to the true next tokens (cross-entropy). "
        "Backpropagation computes how every weight contributed to the error; an optimizer (Adam) nudges weights "
        "to reduce that error. You do not need to derive gradients by hand to understand the architecture — "
        "but you must know that every matmul, softmax, and LayerNorm in the Transformer is differentiable.",
        st["CourseBody"]
    ))
    story.append(P(
        "Checkpoint: if X ∈ R^(T×d), you should instantly know T=tokens, d=features per token, rows=token vectors.",
        st["CourseKey"]
    ))

    story.append(P("1.11 Shape drills (do these mentally)", st["CourseH2"]))
    story.append(mono("""
Drill A: X (5×64), W (64×32) → ?          Answer: (5×32)
Drill B: Q (5×32), K (5×32) → QKᵀ ?       Answer: (5×5)
Drill C: A (5×5), V (5×32) → ?            Answer: (5×32)
Drill D: concat 8 heads of (5×64) → ?     Answer: (5×512)
Drill E: logits (5×10000) softmax on last dim → each row sums to 1
""", st))

    story.append(P("1.12 Notation quick reference", st["CourseH2"]))
    story.append(simple_table([
        ["<b>Symbol</b>", "<b>Meaning</b>"],
        ["T / n", "sequence length"],
        ["d_model / d", "model width"],
        ["d_k, d_v", "key/query and value widths"],
        ["h", "number of heads"],
        ["d_ff", "FFN hidden width"],
        ["N", "number of layers"],
        ["W_Q, W_K, W_V, W_O", "attention projection matrices"],
    ], [1.8*inch, 4.4*inch], st))

    story.append(PageBreak())

    # =====================================================================
    # PART 2
    # =====================================================================
    story.append(P("PART 2 — Why Attention Was Needed", st["PartTitle"]))
    story.append(hr())

    story.append(P("2.1 The story arc", st["CourseH2"]))
    story.append(mono("""
RNN → LSTM → still sequential → long-range pain
   → Attention (decoder looks selectively at encoder states)
   → Self-Attention (tokens attend to tokens in same sequence)
   → Transformer (attention is the whole architecture; no RNN, no CNN)
""", st))

    story.append(P("2.2 Why recurrence is sequential and costly", st["CourseH2"]))
    story.append(P(
        "In an RNN, computing hidden state h_t requires h_{t−1}. GPUs love parallel matrix multiplies, but recurrence "
        "forces a chain through time. For long sentences, training cannot fully parallelize across positions. "
        "Wall-clock training time grows roughly with sequence length even when you have plenty of FLOPs available.",
        st["CourseBody"]
    ))

    story.append(P("2.3 Long-range dependencies (pronoun example)", st["CourseH2"]))
    story.append(P(
        "Example: “The animal didn’t cross the road because <b>it</b> was tired.” "
        "To resolve “it”, the model must relate a pronoun to a noun several tokens away. In deep recurrence, "
        "signals travel many steps and can weaken or be overwritten. Attention creates a direct link in one step: "
        "the query for “it” can put weight directly on the key for “animal”.",
        st["CourseBody"]
    ))
    story.append(mono("""
Distance in sentence:
  animal ----(several tokens)---- it

RNN path length ≈ number of steps between them
Attention path length = 1 (direct score in QKᵀ)
""", st))

    story.append(P("2.4 Why convolutions also struggle for long range", st["CourseH2"]))
    story.append(P(
        "Convolutions see local neighborhoods. Capturing long distance requires many layers or huge kernels, "
        "increasing path length between distant tokens. Attention connects any pair directly (path length O(1)). "
        "This is Table 1’s qualitative argument in the paper.",
        st["CourseBody"]
    ))

    story.append(P("2.5 What attention buys", st["CourseH2"]))
    story.extend(bullets([
        "<b>Selective focus:</b> weight relevant tokens more, ignore others softly",
        "<b>Direct long-range links:</b> any token can influence any other in one layer",
        "<b>Parallelism:</b> all token pairs can be scored with matrix multiplies at once",
    ], st))
    story.append(P(
        "“Parallelization” means: during training, the model can compute attention for the whole sequence "
        "simultaneously instead of waiting token-by-token like an RNN.",
        st["CourseKey"]
    ))

    story.append(P("2.6 From generic attention to self-attention", st["CourseH2"]))
    story.append(P(
        "Earlier seq2seq (Bahdanau et al.) used attention from decoder steps to encoder states — a huge win, "
        "but the backbone was still recurrent. Self-attention goes further: within one sequence, every token "
        "builds a new representation by attending over the same sequence. That is the Transformer’s central move: "
        "make attention the workhorse for representation learning, not just an add-on alignment module.",
        st["CourseBody"]
    ))

    story.append(P("2.7 What would fail without this shift?", st["CourseH2"]))
    story.extend(bullets([
        "Keep RNNs → keep sequential training bottleneck",
        "Keep only local convolutions → keep long path lengths",
        "Keep attention only as decoder→encoder add-on → miss deep contextualization inside each side",
    ], st))
    story.append(P(
        "Paper connection: §1–2 motivate replacing recurrence/convolution with attention; §3 defines the model; "
        "§4 argues complexity / path length; §6 shows BLEU and speed.",
        st["CourseCallout"]
    ))
    story.append(PageBreak())

    # =====================================================================
    # PART 3 — HEAVILY EXPANDED
    # =====================================================================
    story.append(P("PART 3 — Attention From Zero", st["PartTitle"]))
    story.append(hr())
    story.append(P(
        "This is the heart of the paper. Master this section and the rest becomes assembly. "
        "We will compute every intermediate matrix by hand.",
        st["CourseCallout"]
    ))

    story.append(P("3.1 The problem attention solves", st["CourseH2"]))
    story.append(P(
        "Given a question (query), search a set of items (keys), and return a blend of their contents (values), "
        "weighted by how well keys match the query. This is a soft, differentiable dictionary lookup.",
        st["CourseBody"]
    ))

    story.append(P("3.2 Analogy (then we leave the analogy)", st["CourseH2"]))
    story.append(P(
        "Library analogy: Query = what you want; Keys = catalog labels on books; Values = book contents. "
        "You compare query to keys, get relevance weights, then read a weighted mixture of values. "
        "In neural attention, keys and values are vectors, and comparison is a scaled dot product. "
        "After this subsection we speak only in tensors.",
        st["CourseBody"]
    ))

    story.append(P("3.3 Q, K, V without heavy math", st["CourseH2"]))
    story.extend(bullets([
        "<b>Query (Q):</b> “What am I looking for?” — one vector per token asking the question",
        "<b>Key (K):</b> “What do I contain / advertise?” — one vector per token being matched against",
        "<b>Value (V):</b> “What information do I pass if selected?” — content to mix",
    ], st))
    story.append(P(
        "Misconception to avoid: Q/K/V are not three different sentences. In self-attention they are three "
        "different linear projections of the same token representations. In cross-attention, Q comes from the "
        "decoder while K and V come from the encoder.",
        st["CourseWarn"]
    ))

    story.append(P("3.4 The equation", st["CourseH2"]))
    story.append(P("Attention(Q, K, V) = softmax(Q Kᵀ / √d_k) V", st["CourseEq"]))
    story.append(P("Symbol and shape dictionary (batch ignored):", st["CourseBody"]))
    story.extend(bullets([
        "Q ∈ R^(T_q × d_k) — queries",
        "K ∈ R^(T_k × d_k) — keys",
        "V ∈ R^(T_k × d_v) — values (often d_v = d_k)",
        "Kᵀ ∈ R^(d_k × T_k) — transpose of K",
        "QKᵀ ∈ R^(T_q × T_k) — raw similarity scores (every query vs every key)",
        "√d_k — scale factor",
        "A = softmax(QKᵀ/√d_k) ∈ R^(T_q × T_k) — attention weights (each row sums to 1)",
        "output = A V ∈ R^(T_q × d_v) — weighted sum of values for each query",
    ], st))

    story.append(P("3.5 Why divide by √d_k ?", st["CourseH2"]))
    story.append(P(
        "If Q and K have independent components with variance ~1, the dot product has variance ~ d_k. "
        "For large d_k (e.g., 64), scores become large in magnitude → softmax becomes extremely peaky "
        "(almost one-hot) → gradients through softmax vanish. Scaling by √d_k keeps score variance ~1, "
        "so softmax stays informative and trainable.",
        st["CourseBody"]
    ))
    story.append(mono("""
Toy illustration of saturation:
  logits = [10, 0, 0]     → softmax ≈ [1.000, 0.000, 0.000]  (dead gradients for losers)
  logits = [1.0, 0, 0]    → softmax ≈ [0.576, 0.212, 0.212]  (usable gradients)

Scaling prevents the first regime when d_k is large.
""", st))
    story.append(P(
        "Paper statement (§3.2.1) is brief; the underlying reason is softmax saturation under large-variance logits.",
        st["CourseKey"]
    ))

    story.append(P("3.6 Complete numerical example — every intermediate matrix", st["CourseH2"]))
    story.append(P(
        "Setup: 3 tokens, d_k = d_v = 2. We invent Q, K, V directly (as if projections already happened). "
        "Think of the three rows as toy stand-ins for “I”, “love”, “cats”.",
        st["CourseBody"]
    ))
    story.append(mono("""
Token rows:  0="I", 1="love", 2="cats"

Q = [[1.0, 0.0],      # query for "I"
     [0.0, 1.0],      # query for "love"
     [1.0, 1.0]]      # query for "cats"      shape (3,2)

K = [[1.0, 2.0],      # key for "I"
     [0.0, 1.0],      # key for "love"
     [1.0, 0.0]]      # key for "cats"      shape (3,2)

V = [[1.0, 0.0],      # value for "I"
     [0.0, 1.0],      # value for "love"
     [1.0, 1.0]]      # value for "cats"      shape (3,2)
""", st))

    story.append(P("Step A — Transpose K", st["CourseH3"]))
    story.append(mono("""
Kᵀ = [[1.0, 0.0, 1.0],
      [2.0, 1.0, 0.0]]     shape (2,3)
""", st))

    story.append(P("Step B — Raw scores S = Q Kᵀ", st["CourseH3"]))
    story.append(mono("""
S[i,j] = dot(Q[i], K[j])

S[0,0] = 1*1 + 0*2 = 1
S[0,1] = 1*0 + 0*1 = 0
S[0,2] = 1*1 + 0*0 = 1

S[1,0] = 0*1 + 1*2 = 2
S[1,1] = 0*0 + 1*1 = 1
S[1,2] = 0*1 + 1*0 = 0

S[2,0] = 1*1 + 1*2 = 3
S[2,1] = 1*0 + 1*1 = 1
S[2,2] = 1*1 + 1*0 = 1

S = QKᵀ = [[1, 0, 1],
           [2, 1, 0],
           [3, 1, 1]]      shape (3,3)
""", st))

    story.append(P("Step C — Scale by √d_k", st["CourseH3"]))
    story.append(mono("""
√d_k = √2 ≈ 1.41421356
scaled = S / √2

scaled ≈ [[0.7071, 0.0000, 0.7071],
          [1.4142, 0.7071, 0.0000],
          [2.1213, 0.7071, 0.7071]]
""", st))

    story.append(P("Step D — Softmax each row → attention matrix A", st["CourseH3"]))
    story.append(mono("""
Row 0: z=[0.7071, 0.0000, 0.7071]
  exp≈[2.0287, 1.0000, 2.0287]; sum≈5.0575
  A[0]≈[0.4011, 0.1977, 0.4011]

Row 1: z=[1.4142, 0.7071, 0.0000]
  exp≈[4.1133, 2.0287, 1.0000]; sum≈7.1420
  A[1]≈[0.5759, 0.2841, 0.1400]

Row 2: z=[2.1213, 0.7071, 0.7071]
  exp≈[8.3431, 2.0287, 2.0287]; sum≈12.4005
  A[2]≈[0.6728, 0.1636, 0.1636]

A ≈ [[0.401, 0.198, 0.401],
     [0.576, 0.284, 0.140],
     [0.673, 0.164, 0.164]]

Check: each row ≈ 1.0. Cell A[i,j] = how much token i attends to token j.
""", st))

    story.append(P("Step E — Output = A V (weighted mix of values)", st["CourseH3"]))
    story.append(mono("""
out[i] = A[i,0]*V[0] + A[i,1]*V[1] + A[i,2]*V[2]

out0 = 0.401*[1,0] + 0.198*[0,1] + 0.401*[1,1]
     = [0.401, 0] + [0, 0.198] + [0.401, 0.401]
     = [0.802, 0.599]

out1 = 0.576*[1,0] + 0.284*[0,1] + 0.140*[1,1]
     = [0.576, 0] + [0, 0.284] + [0.140, 0.140]
     = [0.716, 0.424]

out2 = 0.673*[1,0] + 0.164*[0,1] + 0.164*[1,1]
     = [0.673, 0] + [0, 0.164] + [0.164, 0.164]
     = [0.837, 0.328]

AttentionOutput ≈ [[0.802, 0.599],
                   [0.716, 0.424],
                   [0.837, 0.328]]     shape (3,2)
""", st))

    story.append(P("3.7 Trace diagram", st["CourseH2"]))
    story.append(mono("""
Input projections → Q, K, V
        │
        ▼
   scores S = Q Kᵀ          (T_q × T_k)
        │
        ▼
   scaled = S / √d_k
        │
        ▼
   A = softmax_row(scaled)  (attention weights)
        │
        ▼
   Out = A V                (T_q × d_v)
""", st))

    story.append(P("3.8 What fails if a piece is removed?", st["CourseH2"]))
    story.extend(bullets([
        "<b>No softmax:</b> weights are not a distribution; mixing is unnormalized and unstable.",
        "<b>No scaling (large d_k):</b> sharp softmax, vanishing gradients, hard training.",
        "<b>No V:</b> you have similarities but no content to pass — matching without readout.",
        "<b>No Q or K:</b> you cannot form content-based addressing; collapses toward fixed averaging.",
    ], st))

    story.append(P("3.9 Where it fits + paper connection", st["CourseH2"]))
    story.append(P(
        "Scaled dot-product attention is the atomic operation inside every Multi-Head Attention block: "
        "encoder self-attention, decoder masked self-attention, and decoder–encoder cross-attention. "
        "Paper: §3.2.1 Scaled Dot-Product Attention; Figure 2 (left).",
        st["CourseBody"]
    ))

    story.append(P("3.10 Second worked example — pronoun toy (T=4, d_k=2)", st["CourseH2"]))
    story.append(P(
        "Tokens: animal, road, it, tired. We hand-craft Q so that “it” matches “animal”.",
        st["CourseBody"]
    ))
    story.append(mono("""
Q = [[0,1], [1,0], [1,1], [0,1]]   # animal, road, it, tired
K = [[1,1], [1,0], [0,1], [0,1]]
V = [[1,0], [0,1], [0,0], [1,1]]

S = QKᵀ =
[[1,0,1,1],
 [1,1,0,0],
 [2,1,1,1],
 [1,0,1,1]]

scaled = S/√2
Row "it" (index 2): z≈[1.414, 0.707, 0.707, 0.707]
A[it] ≈ [0.42, 0.19, 0.19, 0.19]   # largest on animal

out_it mixes values ≈ mostly animal's [1,0] (+ some tired)
→ contextualized "it" carries animal information — coreference in one matmul.
""", st))
    story.append(P(
        "This is the computational form of the linguistic story from Part 2: direct long-range links.",
        st["CourseKey"]
    ))

    story.append(P("3.11 Batch and head dimensions (preview)", st["CourseH2"]))
    story.append(mono("""
In code you usually see:
  Q: (batch, heads, T_q, d_k)
  K: (batch, heads, T_k, d_k)
  V: (batch, heads, T_k, d_v)
  scores: (batch, heads, T_q, T_k)

The math is identical per (batch, head) slice — Part 3 is that slice.
Multi-head (Part 5) runs Part 3 in several subspaces, then concatenates.
""", st))

    story.append(P("3.12 Checklist: can you recompute attention cold?", st["CourseH2"]))
    story.extend(bullets([
        "Write Q,K,V shapes from T and d_k/d_v",
        "Compute one score by hand as a dot product",
        "Scale, softmax one row, check sum≈1",
        "Form one output row as weighted sum of V rows",
        "Name where this sits in Fig. 1",
    ], st))

    story.append(PageBreak())

    # =====================================================================
    # PART 4 — EXPANDED
    # =====================================================================
    story.append(P("PART 4 — Self-Attention", st["PartTitle"]))
    story.append(hr())

    story.append(P("4.1 What makes it “self”?", st["CourseH2"]))
    story.append(P(
        "In self-attention, Q, K, and V all come from the <b>same</b> sequence (after linear projections). "
        "Each token updates itself by looking at every token including itself. This is how a static embedding "
        "becomes a contextualized representation.",
        st["CourseBody"]
    ))

    story.append(P("4.2 From X to Q, K, V", st["CourseH2"]))
    story.append(mono("""
X ∈ R^(T × d_model)          # token vectors (after emb+PE, or previous layer)

W_Q ∈ R^(d_model × d_k)
W_K ∈ R^(d_model × d_k)
W_V ∈ R^(d_model × d_v)

Q = X W_Q                    # (T × d_k)
K = X W_K                    # (T × d_k)
V = X W_V                    # (T × d_v)

A = softmax(Q Kᵀ / √d_k)     # (T × T)
Y = A V                      # (T × d_v)  contextualized (single-head)
""", st))

    story.append(P("4.3 Pronoun sentence — qualitative attention", st["CourseH2"]))
    story.append(P(
        "Sentence: “The animal didn’t cross the road because it was tired.” "
        "For token “it”, a good attention pattern should put substantial mass on “animal” "
        "(the antecedent). Self-attention can learn such links because “it”’s query can match “animal”’s key.",
        st["CourseBody"]
    ))
    story.append(mono("""
Simplified attention row for query="it" (illustrative, not trained weights):

 tokens:  The  animal  didn't  cross  road  because  it  was  tired
 weights: 0.02  0.55    0.02    0.03   0.08   0.05   0.10 0.05  0.10
                              ↑
                     most mass on "animal"
""", st))

    story.append(P("4.4 Attention matrix visualization", st["CourseH2"]))
    story.append(mono("""
Attention weights A (rows = query token, cols = key token):

           The   animal  road   it   tired
The       0.40    0.20   0.15  0.10   0.15
animal    0.10    0.50   0.10  0.10   0.20
road      0.10    0.15   0.45  0.10   0.20
it        0.05    0.55   0.10  0.15   0.15
tired     0.05    0.25   0.10  0.20   0.40

Cell (i,j) = how much token i attends to token j.
Each ROW sums to 1 (after softmax).
""", st))

    story.append(P("4.5 Tiny numerical self-attention with explicit W_Q, W_K, W_V", st["CourseH2"]))
    story.append(P(
        "Now we start from X and projections — not from pre-made Q,K,V. "
        "T=3 tokens (“I”,“love”,“cats”), d_model=2, d_k=d_v=2 (single head toy).",
        st["CourseBody"]
    ))
    story.append(mono("""
X = [[1.0, 0.0],    # I
     [0.0, 1.0],    # love
     [1.0, 1.0]]    # cats         (3×2)

W_Q = [[1, 0],
       [0, 1]]      # identity for clarity
W_K = [[1, 0],
       [0, 1]]
W_V = [[1, 0],
       [0, 1]]

Then Q=X, K=X, V=X.

S = QKᵀ = [[1, 0, 1],
           [0, 1, 1],
           [1, 1, 2]]

scaled = S/√2 ≈ [[0.707, 0.000, 0.707],
                 [0.000, 0.707, 0.707],
                 [0.707, 0.707, 1.414]]

A ≈ [[0.401, 0.198, 0.401],
     [0.212, 0.394, 0.394],
     [0.274, 0.274, 0.452]]

Y = A V = A X ≈
    [[0.802, 0.599],
     [0.606, 0.788],
     [0.726, 0.726]]

Interpretation: each output row is a soft blend of the three input token vectors.
"I" mixes mostly with itself and "cats"; "love" mixes with "love" and "cats"; etc.
""", st))

    story.append(P("4.6 Contextualized representations", st["CourseH2"]))
    story.append(P(
        "After self-attention, a token’s vector is no longer only its embedding. It is a mixture of values from "
        "related tokens — a contextualized representation. Stacking layers deepens this mixing: layer 1 mixes "
        "local/direct relations; deeper layers mix already-mixed signals (higher-order context).",
        st["CourseBody"]
    ))

    story.append(P("4.7 Cost of self-attention", st["CourseH2"]))
    story.append(P(
        "Self-attention compares all pairs → time/memory roughly O(T² · d) for sequence length T. "
        "This is the famous quadratic cost. Worth it for moderate T because of parallelization and short path length. "
        "For very long T, memory for the (T×T) score matrix becomes the bottleneck — motivating later sparse/linear attention.",
        st["CourseBody"]
    ))

    story.append(P("4.8 What fails without self-attention?", st["CourseH2"]))
    story.extend(bullets([
        "Without it inside the encoder: source tokens would not deeply contextualize each other before decoding.",
        "Without it inside the decoder (masked): target tokens could not condition on previous target tokens.",
        "Replacing with RNN: reintroduces sequential bottleneck the paper set out to remove.",
    ], st))
    story.append(P(
        "Paper connection: §3.2. Self-attention is the content of the “Multi-Head Attention” boxes when Q=K=V source.",
        st["CourseCallout"]
    ))

    story.append(P("4.9 Step-by-step: one encoder self-attention for “I love cats”", st["CourseH2"]))
    story.append(mono("""
Goal: contextualize three English tokens before translation.

1. X (3×d) arrives (emb+PE or previous layer)
2. Project: Q,K,V = X W_Q, X W_K, X W_V
3. S = QKᵀ (3×3): how every token scores every token
4. Scale / softmax → A (3×3)
5. Y = A V (3×d_v): each token is now a mixture
6. (In multi-head: do this per head, concat, W^O)
7. Residual+norm with X (Part 8), then FFN (Part 7)

If "cats" should influence "love" (verb-object), A[love, cats] rises after training.
""", st))

    story.append(P("4.10 Self-attention vs bag-of-embeddings", st["CourseH2"]))
    story.append(P(
        "Average-pooling all embeddings is a fixed mixture. Self-attention is a <b>content-dependent</b> mixture: "
        "weights change with the query. That content dependence is why “bank” can mean river or finance "
        "depending on neighbors.",
        st["CourseBody"]
    ))

    story.append(P("4.11 Attention pattern reading practice", st["CourseH2"]))
    story.append(mono("""
Suppose after training, encoder A for "I love cats" looks like:

        I     love   cats
I     0.50   0.30   0.20
love  0.20   0.40   0.40
cats  0.15   0.25   0.60

Reading rows:
- "I" mostly self + some verb
- "love" balances self and object "cats"
- "cats" strongly self (object identity)

These numbers are illustrative; real heads differ and stack across layers.
""", st))

    story.append(PageBreak())

    # =====================================================================
    # PART 5 — EXPANDED
    # =====================================================================
    story.append(P("PART 5 — Multi-Head Attention", st["PartTitle"]))
    story.append(hr())

    story.append(P("5.1 Why one attention head is not enough", st["CourseH2"]))
    story.append(P(
        "A single attention distribution per token is a compromise: one weighting must capture syntax, position, "
        "coreference, and semantics together. Multiple heads let the model attend in several subspaces at once — "
        "different learned projections create different notions of “similarity.”",
        st["CourseBody"]
    ))
    story.append(P(
        "Conceptual examples (not a claim that every head is cleanly interpretable in a trained model): "
        "Head1≈syntax adjacency, Head2≈positional patterns, Head3≈coreference/semantics. "
        "Real heads are messier; the architectural point is capacity for multiple relation types.",
        st["CourseWarn"]
    ))

    story.append(P("5.2 Formula", st["CourseH2"]))
    story.append(P("MultiHead(Q,K,V) = Concat(head_1, …, head_h) W^O", st["CourseEq"]))
    story.append(P("head_i = Attention(Q W_i^Q, K W_i^K, V W_i^V)", st["CourseEq"]))

    story.append(P("5.3 Shapes in the Base model", st["CourseH2"]))
    story.append(mono("""
Paper Base config:
  d_model = 512,  h = 8  →  d_k = d_v = d_model/h = 64

Input X:        (T × 512)
For each head i = 1..8:
  W_i^Q: (512 × 64),  Q_i = X W_i^Q → (T × 64)
  W_i^K: (512 × 64),  K_i = X W_i^K → (T × 64)
  W_i^V: (512 × 64),  V_i = X W_i^V → (T × 64)
  head_i = Attention(Q_i,K_i,V_i) → (T × 64)

Concat heads:   (T × 512)     # 8*64 = 512
W^O:            (512 × 512)
Output:         (T × 512)

Implementation trick: one big Linear(d_model→d_model) for Q, then reshape to (T,h,d_k).
Same for K,V. Mathematically equivalent to separate W_i when dimensions divide evenly.
""", st))

    story.append(P("5.4 Full tiny numerical multi-head example (h=2)", st["CourseH2"]))
    story.append(P(
        "d_model=4, h=2, d_k=2, T=2 tokens. Rows = [“I”, “cats”] toy vectors.",
        st["CourseBody"]
    ))
    story.append(mono("""
X = [[1, 0, 1, 0],     # I
     [0, 1, 0, 1]]     # cats          (2×4)

--- Head 1 projections (toy) ---
Q1 = [[1, 0],          K1 = [[1, 0],        V1 = [[1, 0],
      [0, 1]]               [0, 1]]              [0, 1]]

S1 = Q1 K1ᵀ = [[1, 0],
               [0, 1]]
scaled1 = S1/√2 ≈ [[0.707, 0],
                   [0, 0.707]]
A1 ≈ [[0.668, 0.332],
      [0.332, 0.668]]
head1 = A1 V1 ≈ [[0.668, 0.332],
                 [0.332, 0.668]]

--- Head 2 projections (different subspace) ---
Q2 = [[0, 1],          K2 = [[0, 1],        V2 = [[0, 1],
      [1, 0]]               [1, 0]]              [1, 0]]

S2 = Q2 K2ᵀ = [[1, 0],
               [0, 1]]
A2 ≈ same structure as A1 (in this toy)
head2 ≈ [[0.668, 0.332],
         [0.332, 0.668]]

--- Concatenate ---
concat[0] = [0.668, 0.332, 0.668, 0.332]
concat[1] = [0.332, 0.668, 0.332, 0.668]     # shape (2×4)

--- Output projection W^O (4×4), toy identity ---
Out = concat @ I = concat

If W^O were not identity, it would mix head channels into final features.
""", st))

    story.append(P("5.5 ASCII picture of multi-head", st["CourseH2"]))
    story.append(mono("""
                 X (T × d_model)
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
     head_1      head_2  ...  head_h
     (T×d_k)     (T×d_k)      (T×d_k)
        │           │           │
        └───── concat (T × h*d_k) ─────┘
                    │
                    ▼
                 × W^O
                    │
                    ▼
              Out (T × d_model)
""", st))

    story.append(P("5.6 What fails if multi-head is removed?", st["CourseH2"]))
    story.append(P(
        "Single-head with same compute budget has less ability to represent multiple incompatible attention "
        "patterns at once. Ablations in the paper show that reducing heads (while holding compute roughly "
        "constant via d_k) hurts quality past a point — diversity of subspaces matters.",
        st["CourseBody"]
    ))
    story.append(P(
        "Paper connection: §3.2.2 Multi-Head Attention; Figure 2 (right); ablation tables on number of heads.",
        st["CourseCallout"]
    ))

    story.append(P("5.7 Parameter counting (Base, one MHA module)", st["CourseH2"]))
    story.append(mono("""
W_Q, W_K, W_V, W_O each: 512×512 (+ biases optional)
≈ 4 * 512 * 512 = 1,048,576 weights for projections alone per MHA block.

Encoder: 6 layers → 6 self-attn MHAs
Decoder: 6 layers → 6 masked self-attn + 6 cross-attn = 12 MHAs
Attention projections + FFNs dominate Base parameter count.
""", st))

    story.append(P("5.8 Common implementation reshape", st["CourseH2"]))
    story.append(mono("""
x: (B,T,512)
q = W_q(x): (B,T,512)
q = q.view(B,T,8,64).transpose(1,2) → (B,8,T,64)
# batched attention over heads
# reverse to concat: transpose + contiguous view → (B,T,512)
""", st))

    story.append(P("5.9 Heads are not free interpretability", st["CourseH2"]))
    story.append(P(
        "Papers and blogs sometimes label heads (“syntax head”, “anaphora head”). Treat such labels as "
        "hypotheses. Architecturally, multi-head guarantees capacity for multiple patterns — not that "
        "each head learns a clean linguistic category.",
        st["CourseWarn"]
    ))

    story.append(PageBreak())

    # =====================================================================
    # PART 6 — EXPANDED
    # =====================================================================
    story.append(P("PART 6 — Positional Encoding", st["PartTitle"]))
    story.append(hr())

    story.append(P("6.1 The problem", st["CourseH2"]))
    story.append(P(
        "Self-attention is permutation-equivariant over positions if we only feed token embeddings: "
        "shuffling tokens would produce shuffled outputs with the same pairwise scores structure. "
        "Word order matters (“dog bites man” ≠ “man bites dog”). Without position information, "
        "the model is closer to a bag-of-vectors mixer.",
        st["CourseBody"]
    ))
    story.append(mono("""
If PE is absent:
  Attention(X) for [A,B,C]  vs  Attention(X) for [C,B,A]
  → outputs are the same vectors permuted — order not represented.
""", st))

    story.append(P("6.2 The 2017 solution: sinusoidal PE added to embeddings", st["CourseH2"]))
    story.append(P("PE(pos, 2i)   = sin(pos / 10000^(2i/d_model))", st["CourseEq"]))
    story.append(P("PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))", st["CourseEq"]))
    story.extend(bullets([
        "pos = token position (0, 1, 2, …)",
        "i = dimension-pair index (0 … d_model/2 − 1)",
        "even dims use sin; odd dims use cos",
        "different frequencies across dimensions → unique patterns per position",
    ], st))

    story.append(P("6.3 Why add (not concatenate)?", st["CourseH2"]))
    story.append(P(
        "Adding keeps shape (T × d_model) unchanged and injects position into the same space the model already uses. "
        "No extra width; residual pathway stays clean. The network learns to use the combined signal. "
        "Concatenation would change d_model or require an immediate projection.",
        st["CourseBody"]
    ))

    story.append(P("6.4 Why sine/cosine?", st["CourseH2"]))
    story.append(P(
        "The paper argues relative positions can be expressed as linear functions of these encodings "
        "(useful for attending by offset), and they can extrapolate to sequence lengths longer than those "
        "seen in training. Absolute learned position embeddings were also tried and performed similarly "
        "on the paper’s tasks — but sinusoids were chosen for the extrapolation argument.",
        st["CourseBody"]
    ))
    story.append(P(
        "Modern models often use learned absolute, relative, or RoPE positions — different from original 2017. "
        "Do not silently replace sinusoids when explaining this paper.",
        st["CourseWarn"]
    ))

    story.append(P("6.5 Worked PE numbers (d_model=4)", st["CourseH2"]))
    story.append(mono("""
d_model=4 → dimension pairs i=0 and i=1

For i=0: 10000^(2*0/4) = 10000^0 = 1
For i=1: 10000^(2*1/4) = 10000^(0.5) = 100

Position 0:
  PE(0,0)=sin(0/1)=0
  PE(0,1)=cos(0/1)=1
  PE(0,2)=sin(0/100)=0
  PE(0,3)=cos(0/100)=1
  PE[0] = [0, 1, 0, 1]

Position 1:
  PE(1,0)=sin(1/1)=sin(1)≈0.8415
  PE(1,1)=cos(1/1)=cos(1)≈0.5403
  PE(1,2)=sin(1/100)=sin(0.01)≈0.0100
  PE(1,3)=cos(1/100)=cos(0.01)≈0.99995
  PE[1] ≈ [0.8415, 0.5403, 0.0100, 1.0000]

Position 2:
  PE(2,0)=sin(2)≈0.9093
  PE(2,1)=cos(2)≈-0.4161
  PE(2,2)=sin(0.02)≈0.0200
  PE(2,3)=cos(0.02)≈0.9998
  PE[2] ≈ [0.9093, -0.4161, 0.0200, 0.9998]

Notice: low dimensions (i=0) change quickly with pos;
high dimensions (i=1) change slowly — multi-scale position signal.
""", st))

    story.append(P("6.6 Adding PE to our translation example", st["CourseH2"]))
    story.append(mono("""
Source tokens: I, love, cats     positions 0,1,2
Suppose toy embeddings E (3×4):
E = [[0.1, 0.2, 0.3, 0.4],
     [0.5, 0.1, 0.0, 0.2],
     [0.2, 0.4, 0.1, 0.3]]

X0 = E + PE[0:3]
X0[0] = [0.1, 0.2, 0.3, 0.4] + [0, 1, 0, 1]     = [0.1, 1.2, 0.3, 1.4]
X0[1] = [0.5, 0.1, 0.0, 0.2] + [0.84, 0.54, 0.01, 1.00] ≈ [1.34, 0.64, 0.01, 1.20]
X0[2] ≈ [0.2, 0.4, 0.1, 0.3] + [0.91, -0.42, 0.02, 1.00] ≈ [1.11, -0.02, 0.12, 1.30]

This X0 is the encoder stack's input.
""", st))

    story.append(P("6.7 What fails without PE?", st["CourseH2"]))
    story.append(P(
        "Order confusion / bag-of-vectors behavior. The model cannot reliably distinguish "
        "“I love cats” from “cats love I”. Architecture would not know sequence order.",
        st["CourseWarn"]
    ))
    story.append(P(
        "Paper connection: §3.5 Positional Encoding; also compared to learned embeddings.",
        st["CourseCallout"]
    ))

    story.append(P("6.8 Relative-position intuition from sinusoids", st["CourseH2"]))
    story.append(P(
        "Because sin/cos of different frequencies behave like a geometric progression, there exist linear "
        "transforms relating PE(pos+k) to PE(pos). The paper cites this as a reason the model can learn "
        "to attend by relative offset. You do not need the trig proof to use PE — but it explains why "
        "random fixed vectors would be a weaker inductive bias.",
        st["CourseBody"]
    ))

    story.append(P("6.9 Decoder PE is independent", st["CourseH2"]))
    story.append(P(
        "Encoder and decoder each add PE to their own embeddings. Position 0 on the English side is not "
        "the same slot as position 0 on the French side; each sequence has its own timeline. "
        "Cross-attention aligns them by content, not by forcing equal indices.",
        st["CourseBody"]
    ))
    story.append(mono("""
Source positions:  0:I    1:love    2:cats
Target positions:  0:BOS  1:J'aime  2:les  3:chats

Cross-attn may map target pos3 → source pos2 even though indices differ.
""", st))

    story.append(P("6.10 PE frequency table (d_model=8, pos=0..3)", st["CourseH2"]))
    story.append(mono("""
i=0 denom=1; i=1 denom=10; i=2 denom=100; i=3 denom=1000  (approx via 10000^(2i/8))

pos/dim  0(sin)   1(cos)   2(sin)   3(cos)   4(sin)   5(cos) ...
0         0.000    1.000    0.000    1.000    0.000    1.000
1         0.841    0.540    0.100    0.995    0.010    1.000
2         0.909   -0.416    0.199    0.980    0.020    1.000
3         0.141   -0.990    0.296    0.955    0.030    1.000

Low dims oscillate fast (fine position); high dims change slowly (coarse position).
""", st))

    story.append(PageBreak())

    # =====================================================================
    # PART 7
    # =====================================================================
    story.append(P("PART 7 — The Feed-Forward Network", st["PartTitle"]))
    story.append(hr())
    story.append(P("FFN(x) = max(0, x W_1 + b_1) W_2 + b_2", st["CourseEq"]))

    story.append(P("7.1 Why FFN after attention?", st["CourseH2"]))
    story.append(P(
        "Attention mixes information <b>across tokens</b> (communication). The FFN processes each token "
        "independently, applying a nonlinear transform — “thinking” content-wise after communication. "
        "Attention alone is mostly linear mixing of values (plus softmax nonlinearity on weights); "
        "deep nonlinear per-token capacity comes largely from the FFN.",
        st["CourseBody"]
    ))

    story.append(P("7.2 Expansion and contraction", st["CourseH2"]))
    story.append(mono("""
x:   (T × d_model)        e.g., 512
W1:  (d_model × d_ff)     e.g., 512 → 2048
hidden = ReLU(x W1 + b1)  (T × 2048)
W2:  (d_ff × d_model)     2048 → 512
out: (T × d_model)

Same FFN weights shared across positions; applied independently per position.
In Base model, FFN holds a large fraction of parameters (two big matrices).
""", st))

    story.append(P("7.3 Tiny numerical FFN", st["CourseH2"]))
    story.append(mono("""
One token x = [1.0, -0.5] , d_model=2, d_ff=4

W1 = [[1, 0, 1, 0],
      [0, 1, 0, 1]]          # (2×4)
b1 = [0, 0, 0, 0]
h_pre = x W1 = [1.0, -0.5, 1.0, -0.5]
h = ReLU(h_pre) = [1.0, 0.0, 1.0, 0.0]

W2 = [[0.5, 0.0],
      [0.0, 0.5],
      [0.5, 0.0],
      [0.0, 0.5]]          # (4×2)
out = h W2 = [1.0, 0.0]

ReLU zeroed the negative channels — nonlinearity that stacked linear maps cannot mimic.
""", st))

    story.append(P("7.4 What fails without FFN / without ReLU?", st["CourseH2"]))
    story.extend(bullets([
        "Without FFN: layers mostly remix existing features; limited per-token nonlinear computation.",
        "Without ReLU (or other nonlinearity): stacked linear maps collapse to one linear map; expressive power drops.",
    ], st))
    story.append(P(
        "Paper connection: §3.3 Position-wise Feed-Forward Networks. Note: applied identically at each position.",
        st["CourseCallout"]
    ))

    story.append(P("7.5 FFN as “key-value memory” intuition (optional)", st["CourseH2"]))
    story.append(P(
        "Some analyses view the expanded ReLU layer as detecting features (W1 rows/columns as keys) and "
        "writing values (W2). You do not need this view to implement the paper, but it explains why d_ff ≫ d_model "
        "helps: more feature detectors per token after attention mixing.",
        st["CourseBody"]
    ))
    story.append(P("7.6 Where FFN sits relative to attention", st["CourseH2"]))
    story.append(mono("""
Attention:  tokens talk to each other      (across-T mix)
FFN:        each token thinks alone        (across-d nonlinear)

Stacking them = communicate, then compute, repeatedly.
""", st))
    story.append(PageBreak())

    # =====================================================================
    # PART 8 — Post-LN vs Pre-LN
    # =====================================================================
    story.append(P("PART 8 — Residual Connections + Layer Normalization", st["PartTitle"]))
    story.append(hr())
    story.append(P(
        "Deep Transformers need two engineering ideas that are easy to skip when staring at attention: "
        "residuals (so layers refine rather than overwrite) and normalization (so scales stay trainable). "
        "The 2017 paper’s specific order is Post-LN — memorize it.",
        st["CourseCallout"]
    ))

    story.append(P("8.1 Residual connection intuition", st["CourseH2"]))
    story.append(P(
        "Instead of replacing a representation with Sublayer(x), use x + Sublayer(x). "
        "The sublayer learns a refinement (residual) rather than a full rewrite. This eases gradient flow "
        "in deep stacks (N=6 encoder + N=6 decoder is already deep for 2017).",
        st["CourseBody"]
    ))
    story.append(mono("output_raw = x + MultiHeadAttention(x)   # same idea for FFN", st))

    story.append(P("8.2 Layer normalization", st["CourseH2"]))
    story.append(P(
        "LayerNorm normalizes features of each token (across the d_model dimension) to stable mean/variance, "
        "then applies learned scale γ and bias β. Stabilizes training of deep networks. "
        "Unlike BatchNorm, it does not depend on batch statistics — natural for variable-length sequences.",
        st["CourseBody"]
    ))
    story.append(mono("""
For one token vector x ∈ R^d:
  μ = mean(x);  σ² = variance(x)
  x̂ = (x − μ) / √(σ² + ε)
  y = γ ⊙ x̂ + β
""", st))

    story.append(P("8.3 Original 2017: Post-LN (Add & Norm)", st["CourseH2"]))
    story.append(P("LayerNorm( x + Sublayer(x) )", st["CourseEq"]))
    story.append(P(
        "Order: compute sublayer → add residual → LayerNorm. This is <b>Post-LN</b>. "
        "Figure 1’s “Add & Norm” boxes mean exactly this.",
        st["CourseBody"]
    ))
    story.append(mono("""
# Original paper encoder block (Post-LN):
y = LayerNorm( x + Dropout(SelfAttn(x)) )
z = LayerNorm( y + Dropout(FFN(y)) )
""", st))

    story.append(P("8.4 Modern contrast: Pre-LN", st["CourseH2"]))
    story.append(mono("""
# Common modern Pre-LN block:
y = x + Dropout(SelfAttn(LayerNorm(x)))
z = y + Dropout(FFN(LayerNorm(y)))
# often final LayerNorm at the very end of the stack
""", st))
    story.append(P(
        "Pre-LN often trains more stably for very deep stacks and is common in GPT-style models. "
        "<b>Do not silently substitute Pre-LN when explaining the 2017 paper.</b> "
        "If you implement Post-LN vs Pre-LN wrong, you are not reproducing Vaswani et al.",
        st["CourseWarn"]
    ))

    story.append(P("8.5 Side-by-side", st["CourseH2"]))
    story.append(simple_table([
        ["<b>Aspect</b>", "<b>Post-LN (2017)</b>", "<b>Pre-LN (modern)</b>"],
        ["Norm position", "After residual add", "Before sublayer"],
        ["Paper Fig. 1", "Matches", "Does not match"],
        ["Deep training", "Can need careful LR", "Often stabler deep"],
        ["Output scale", "Normed every block", "Residual path un-normed"],
    ], [1.5*inch, 2.2*inch, 2.5*inch], st))

    story.append(P("8.6 What fails without residuals / norms?", st["CourseH2"]))
    story.extend(bullets([
        "Without residuals: deep stacks become hard to optimize; gradients degrade.",
        "Without LayerNorm: activation scales drift; training unstable.",
        "Wrong order (Pre vs Post): may still train, but it is a different architecture than the paper.",
    ], st))
    story.append(PageBreak())

    # =====================================================================
    # PART 9
    # =====================================================================
    story.append(P("PART 9 — Build the Encoder From Scratch", st["PartTitle"]))
    story.append(hr())

    story.append(P("9.1 One encoder layer (2017 Post-LN)", st["CourseH2"]))
    story.append(mono("""
One Encoder Layer:

Input X (T × d_model)
  │
  ├─ Multi-Head Self-Attention
  │     Q,K,V all from X
  │
  ├─ Dropout on attention output
  ├─ Add & Norm:  LayerNorm(X + Attn)     # Post-LN
  │
  ├─ Position-wise FFN (ReLU expand/contract)
  │
  ├─ Dropout on FFN output
  └─ Add & Norm:  LayerNorm(Y + FFN)
        │
        ▼
Output (T × d_model)   # same shape as input
""", st))

    story.append(P("9.2 Stacking N=6", st["CourseH2"]))
    story.append(P(
        "Base Transformer stacks N=6 identical encoder layers (shared structure, separate parameters). "
        "Lower layers often capture more local/surface patterns; higher layers more abstract combinations — "
        "not a rigid law, but why depth helps: repeated mix (attention) + transform (FFN).",
        st["CourseBody"]
    ))
    story.append(mono("""
X0 = Embedding(src_ids) * √d_model + PE
X1 = EncoderLayer1(X0)
X2 = EncoderLayer2(X1)
...
X6 = EncoderLayer6(X5)
Memory M = X6     # contextual source for decoder cross-attention
""", st))
    story.append(P(
        "Note: the paper scales embeddings by √d_model before adding PE.",
        st["CourseKey"]
    ))

    story.append(P("9.3 Running example shapes (“I love cats”)", st["CourseH2"]))
    story.append(mono("""
Source T_src = 3, d_model = 512 (paper) or 8 (toy)

ids → Emb (3×512) → *√512 → +PE → X0 (3×512)
6 × EncoderLayer → M (3×512)

Each layer preserves (3×512). Only internal Q/K/V widths are 64 per head.
""", st))

    story.append(P("9.4 What the encoder is for", st["CourseH2"]))
    story.append(P(
        "Encoder output is a contextualized sequence of source tokens — memory for the decoder to attend over. "
        "It is not yet French words; it is a rich English-side representation.",
        st["CourseKey"]
    ))

    story.append(P("9.5 Encoder-only vs full Transformer", st["CourseH2"]))
    story.append(P(
        "If you chop off the decoder and add a classification head, you get an encoder-only model family "
        "(BERT-like). That is later work. The 2017 paper’s MT system needs both stacks.",
        st["CourseBody"]
    ))
    story.append(P("9.6 Numerical residual step inside encoder", st["CourseH2"]))
    story.append(mono("""
Toy d_model=2, one token:
x = [1.0, 2.0]
attn_out = [0.2, -0.5]
x1_pre = x + attn_out = [1.2, 1.5]
x1 = LayerNorm(x1_pre)   # mean/var normalize then γ,β

ffn_out = [0.1, 0.1]
x2 = LayerNorm(x1 + ffn_out)

Shape unchanged; content refined. Repeat N times.
""", st))
    story.append(PageBreak())

    # =====================================================================
    # PART 10 — EXPANDED
    # =====================================================================
    story.append(P("PART 10 — The Decoder (Masking + Cross-Attention)", st["PartTitle"]))
    story.append(hr())

    story.append(P("10.1 Why the decoder differs", st["CourseH2"]))
    story.append(P(
        "The decoder must generate the target left-to-right without cheating by looking at future target tokens. "
        "It also must read the encoder’s source representations. So each decoder layer needs three sublayers: "
        "(1) masked self-attention, (2) cross-attention, (3) FFN — each wrapped with Add & Norm (Post-LN).",
        st["CourseBody"]
    ))

    story.append(P("10.2 Causal masking (look-ahead mask) — detailed", st["CourseH2"]))
    story.append(P(
        "During training, the full target sentence exists in the batch. Without a mask, self-attention would let "
        "position i see positions > i — information leakage from the future. The causal mask sets future scores "
        "to −∞ before softmax so those weights become 0.",
        st["CourseBody"]
    ))
    story.append(mono("""
Target: "<BOS> J'aime les chats"   (predicting French)

Causal mask M (0=allowed shown as 0, blocked as -inf before softmax):

           BOS   J'aime  les   chats
BOS         0     -inf   -inf   -inf
J'aime      0       0    -inf   -inf
les         0       0      0    -inf
chats       0       0      0      0

Rule: query position i may only see keys j ≤ i.
After softmax, each row is a distribution over the allowed prefix only.
""", st))

    story.append(P("10.3 Numerical masked attention (tiny)", st["CourseH2"]))
    story.append(mono("""
T=3, d_k=2, ignore projections; Q=K=V given:

Q=K = [[1,0],[0,1],[1,1]]
S = QKᵀ = [[1,0,1],
           [0,1,1],
           [1,1,2]]

Apply causal mask (set j>i to -inf):
S_masked = [[1,  -inf, -inf],
            [0,   1,   -inf],
            [1,   1,    2 ]]

scaled = S_masked / √2
A = softmax_row(scaled)

Row0: only pos0 → A[0] = [1, 0, 0]
Row1: pos0,1 → softmax([0, 0.707]) ≈ [0.332, 0.668, 0]
Row2: all three → as unmasked row for [0.707,0.707,1.414]

Without mask, row0 could put weight on future tokens — illegal for autoregressive MT.
""", st))

    story.append(P("10.4 Cross-attention (encoder–decoder attention)", st["CourseH2"]))
    story.append(P(
        "After masked self-attention, each decoder position needs source information. Cross-attention uses:",
        st["CourseBody"]
    ))
    story.append(mono("""
Q = from decoder states     shape (T_tgt × d_k)
K = from encoder memory M   shape (T_src × d_k)
V = from encoder memory M   shape (T_src × d_v)

Scores: (T_tgt × T_src) — each French position looks over English positions.

Running example alignments (illustrative):
  "J'aime" attends strongly to "love" (and maybe "I")
  "les"    may attend to function-word structure
  "chats"  attends strongly to "cats"
""", st))

    story.append(P("10.5 One decoder layer ASCII", st["CourseH2"]))
    story.append(mono("""
Y_in (T_tgt × d_model)
  │
  ├─ Masked Multi-Head Self-Attention (Q=K=V=Y)
  ├─ Add & Norm (Post-LN)
  │
  ├─ Multi-Head Cross-Attention (Q=Y, K=V=Memory)
  ├─ Add & Norm
  │
  ├─ FFN
  └─ Add & Norm
        │
        ▼
Y_out (T_tgt × d_model)
""", st))

    story.append(P("10.6 Training decoder input (teacher forcing, shifted right)", st["CourseH2"]))
    story.append(mono("""
Target gold:     J'aime   les   chats   <EOS>
Decoder input:   <BOS>    J'aime les    chats
Predict:         J'aime   les   chats   <EOS>

Position t's prediction is trained against gold token t,
while only attending to decoder inputs ≤ t (via mask).
""", st))

    story.append(P("10.7 What fails if masking / cross-attention is removed?", st["CourseH2"]))
    story.extend(bullets([
        "<b>No causal mask:</b> model cheats during training; inference (no future tokens) mismatches train — poor generation.",
        "<b>No cross-attention:</b> decoder never reads source; cannot translate, only babble target language models.",
        "<b>No masked self-attention:</b> no target-side language modeling / fluency conditioning.",
    ], st))
    story.append(P(
        "Paper connection: §3.1 decoder; §3.2.3 “Applications of Attention” (self / masked / encoder-decoder).",
        st["CourseCallout"]
    ))

    story.append(P("10.8 Three attention types in one diagram", st["CourseH2"]))
    story.append(mono("""
ENCODER self-attention:
  Q,K,V from source; full (unmasked) T_src × T_src

DECODER masked self-attention:
  Q,K,V from target; causal T_tgt × T_tgt

DECODER cross-attention:
  Q from target; K,V from encoder memory; T_tgt × T_src

All three are the SAME Attention(Q,K,V) function with different inputs/masks.
""", st))

    story.append(P("10.9 Padding masks (practical detail)", st["CourseH2"]))
    story.append(P(
        "Batches pad short sentences to a common length. Padding positions should not be attended to: "
        "set their key scores to −∞ as well (separate from causal masking). Causal mask ∧ padding mask "
        "are both applied before softmax in real systems.",
        st["CourseBody"]
    ))
    story.append(mono("""
Example src batch (pad=0):
  [I, love, cats, PAD]
  mask_key = [1,1,1,0]  → column PAD blocked for all queries
""", st))

    story.append(P("10.10 Worked cross-attention scores (toy)", st["CourseH2"]))
    story.append(mono("""
T_tgt=2 ("J'aime","chats"), T_src=3 ("I","love","cats"), d_k=2

Q_dec = [[1,0],      # J'aime
         [0,1]]      # chats
K_enc = [[1,0],      # I
         [1,1],      # love
         [0,1]]      # cats
V_enc = [[0,0],[1,0],[0,1]]

S = Q Kᵀ = [[1,1,0],
            [0,1,1]]
A ≈ softmax(S/√2):
  J'aime row peaks on I/love
  chats  row peaks on love/cats

Out = A V mixes encoder values into decoder positions.
""", st))

    story.append(P("10.11 Layer stack reminder", st["CourseH2"]))
    story.append(P(
        "N=6 means this three-sublayer recipe repeats six times. Early decoder layers may focus more on "
        "local target syntax; later layers often strengthen cross-lingual alignment — again a tendency, not a law.",
        st["CourseBody"]
    ))

    story.append(PageBreak())

    # =====================================================================
    # PART 11 — EXPANDED
    # =====================================================================
    story.append(P("PART 11 — Complete Transformer Data Flow", st["PartTitle"]))
    story.append(hr())
    story.append(P(
        "We now mentally simulate the full system for: “I love cats” → “J’aime les chats”.",
        st["CourseCallout"]
    ))

    story.append(P("11.1 End-to-end ASCII", st["CourseH2"]))
    story.append(mono("""
 SOURCE: I love cats                     TARGET: J'aime les chats
        │                                       │
        ▼                                       ▼
   Token IDs                               Token IDs (+BOS shift)
        │                                       │
        ▼                                       ▼
   Embedding ×√d_model                     Embedding ×√d_model
        │                                       │
        ▼                                       ▼
   + Positional Encoding                   + Positional Encoding
        │                                       │
        ▼                                       ▼
   ┌─────────────────┐                   ┌──────────────────────┐
   │ Encoder × N=6   │                   │ Decoder × N=6        │
   │  self-attn      │                   │  masked self-attn    │
   │  FFN            │────── Memory M ──▶│  cross-attn (to M)   │
   │  (Post-LN)      │                   │  FFN (Post-LN)       │
   └─────────────────┘                   └──────────┬───────────┘
                                                    ▼
                                            Linear → vocab logits
                                                    ▼
                                               Softmax → probs
                                                    ▼
                                          Loss vs gold target tokens
""", st))

    story.append(P("11.2 Shape trace (toy d_model=8, paper note in comments)", st["CourseH2"]))
    story.append(mono("""
Assume d_model=8, h=2, d_k=4, d_ff=32, V_vocab=1000  (paper: 512/8/64/2048/~32k)

1) Source tokenize: ["I","love","cats"] → ids (3,)
2) Emb_s: (3×8); scale √8; +PE → X0 (3×8)
3) Encoder layer (repeat 6×):
     Q,K,V projections → heads → concat → (3×8)
     Add&Norm → FFN → Add&Norm → still (3×8)
   Memory M: (3×8)

4) Decoder inputs (teacher forcing):
   ["<BOS>","J'aime","les","chats"] → Y0 (4×8) after emb+PE

5) Decoder layer (repeat 6×):
   a) masked self-attn on Y: scores (4×4) with causal mask → (4×8)
   b) cross-attn: Q from Y (4×d_k), K/V from M (3×d_k)
      scores (4×3) → output (4×8)
   c) FFN → (4×8)

6) Final linear: (4×8) @ W_vocab(8×1000) → logits (4×1000)
7) Softmax over vocab dim → probs (4×1000)
8) Cross-entropy vs gold ["J'aime","les","chats","<EOS>"]

Mental rule: every block preserves (T × d_model) until the final vocab projection.
""", st))

    story.append(P("11.3 Token-level story (one French word)", st["CourseH2"]))
    story.append(P(
        "When the decoder is at the position that should predict “chats”:",
        st["CourseBody"]
    ))
    story.extend(bullets([
        "Masked self-attn lets it read &lt;BOS&gt;, J’aime, les (not future).",
        "Cross-attn lets it look at contextualized “I”,“love”,“cats” — ideally heavy on “cats”.",
        "FFN nonlinearly transforms that mixture.",
        "Final linear+softmax puts high probability on “chats”.",
    ], st))

    story.append(P("11.4 Training vs inference dataflow difference", st["CourseH2"]))
    story.append(mono("""
TRAINING:
  full target available → parallel teacher forcing over all tgt positions
  causal mask prevents cheating
  one forward pass over whole target length

INFERENCE:
  encode source once → M
  generate y1, then y2, ... sequentially
  each step runs decoder on prefix generated so far
  stop at <EOS> or max length
""", st))
    story.append(P(
        "Same architecture weights; different iteration pattern over the decoder.",
        st["CourseKey"]
    ))

    story.append(P("11.5 Full tensor diary (write this on paper once)", st["CourseH2"]))
    story.append(mono("""
Let d=512, h=8, d_k=64, N=6, V=~32000

src_ids:        (B, 3)
src_emb:        (B, 3, 512)
src_x:          (B, 3, 512)   # *sqrt(d)+PE
after enc:      (B, 3, 512)   # Memory

tgt_ids_in:     (B, 4)
tgt_x:          (B, 4, 512)
after dec:      (B, 4, 512)
logits:         (B, 4, V)
loss:           scalar

Inside one MHA:
  qkv: (B,4,512) → split (B,8,4,64)
  scores self: (B,8,4,4)   or cross (B,8,4,3)
""", st))

    story.append(P("11.6 Where information moves", st["CourseH2"]))
    story.extend(bullets([
        "Encoder self-attn: English ↔ English",
        "Decoder masked self-attn: French prefix ↔ French prefix",
        "Cross-attn: French ↔ English",
        "FFN: within-token feature remix (no inter-token mix)",
        "Final linear: features → vocabulary evidence",
    ], st))

    story.append(P("11.7 Failure modes mapped to missing pieces", st["CourseH2"]))
    story.append(mono("""
Symptoms → likely missing piece
-------------------------------
Ignores word order           → PE
Can't resolve "it"           → self-attention depth/capacity
Translates without source    → cross-attention
Copies future target words   → causal mask (train/test mismatch)
Deep net won't train         → residuals / LayerNorm (and LR schedule)
Fluent but wrong meaning     → weak cross-attn / undertrained encoder
""", st))

    story.append(PageBreak())

    # =====================================================================
    # PART 12 — EXPANDED
    # =====================================================================
    story.append(P("PART 12 — Training the Transformer", st["PartTitle"]))
    story.append(hr())

    story.append(P("12.1 Teacher forcing and shifted targets", st["CourseH2"]))
    story.extend(bullets([
        "<b>Teacher forcing:</b> feed the correct previous target tokens as decoder input (not the model’s own previous guesses).",
        "<b>Shifted inputs:</b> decoder sees tokens up to t−1 when predicting token t.",
        "<b>Why:</b> enables parallel training over time; stabilizes early learning.",
    ], st))
    story.append(mono("""
Example batch item:
  src:  I love cats
  tgt_in:  <BOS> J'aime les chats
  tgt_out: J'aime les chats <EOS>
""", st))

    story.append(P("12.2 Logits, softmax, cross-entropy", st["CourseH2"]))
    story.append(mono("""
At one position, vocab {A,B,C}:
logits = [2.0, 0.5, 0.1]
probs  = softmax(logits) ≈ [0.659, 0.242, 0.099]
true = A → loss = -log(0.659) ≈ 0.417

Full sequence loss = average -log p(true_t) over non-pad positions.
""", st))

    story.append(P("12.3 Label smoothing (paper detail)", st["CourseH2"]))
    story.append(P(
        "Instead of hard 1-hot targets, the paper uses label smoothing with ε_ls=0.1: "
        "the correct class gets 1−ε, and the remaining ε is spread over other classes. "
        "This penalizes overconfidence and improved BLEU in their experiments. "
        "It is a training procedure detail, not an architecture change.",
        st["CourseBody"]
    ))

    story.append(P("12.4 Optimizer and learning-rate schedule", st["CourseH2"]))
    story.append(P(
        "Adam with β1=0.9, β2=0.98, ε=10^−9. Learning rate follows a formula with warmup: "
        "increase linearly for warmup_steps (4000), then decay proportionally to step^(−0.5). "
        "This schedule is important to reproduce paper results — architecture alone is not enough.",
        st["CourseBody"]
    ))
    story.append(mono("""
lrate = d_model^(-0.5) * min(step^(-0.5), step * warmup^(-1.5))
""", st))

    story.append(P("12.5 Regularization", st["CourseH2"]))
    story.extend(bullets([
        "Dropout P_drop=0.1 on attention weights / residual paths / embeddings as specified",
        "Residual dropout after each sublayer before Add & Norm",
    ], st))

    story.append(P("12.6 What gradients flow through", st["CourseH2"]))
    story.append(P(
        "Gradients flow through softmax, final linear, decoder stack (including attention weights and Q/K/V), "
        "cross-attention into encoder memory, encoder stack, embeddings. "
        "Attention’s softmax and matmuls are fully differentiable — that is why attention is trainable.",
        st["CourseBody"]
    ))

    story.append(P("12.7 Mini training step checklist", st["CourseH2"]))
    story.append(mono("""
1. Embed+PE source and shifted target
2. Encode source → M
3. Decode with causal mask + cross-attn to M → logits
4. Compute CE (optionally label-smoothed) vs gold next tokens
5. backward(); Adam step with scheduled LR
6. repeat
""", st))

    story.append(P("12.8 Worked micro-batch loss", st["CourseH2"]))
    story.append(mono("""
Suppose V=4 tokens {BOS, J'aime, les, chats}, ignore real vocab size.

At position predicting "les":
  logits = [0.1, 0.2, 2.5, 0.3]   # classes 0..3
  p(les)=softmax ≈ 0.80
  CE = -log(0.80) ≈ 0.223

At position predicting "chats":
  logits = [0.0, 0.1, 0.2, 1.5]
  p ≈ 0.55 → CE ≈ 0.598

Mean loss ≈ 0.41 for these two positions.
Backprop increases logits of correct classes on the next update.
""", st))

    story.append(P("12.9 What training is NOT", st["CourseH2"]))
    story.extend(bullets([
        "Not searching attention patterns by hand — gradients discover them",
        "Not requiring force-aligned word dictionaries (attention learns soft alignment)",
        "Not identical to inference compute graph over time (teacher forcing vs autoregressive)",
    ], st))

    story.append(P("12.10 Gradient intuition through attention", st["CourseH2"]))
    story.append(P(
        "If the model assigned too little weight to “cats” when predicting “chats”, the loss gradient "
        "encourages increasing the score Q_chats·K_cats (via W_Q/W_K) and/or adjusting V_cats and W_O. "
        "You rarely debug this by hand — but knowing the pathway demystifies “attention learns alignments.”",
        st["CourseBody"]
    ))

    story.append(PageBreak())

    # =====================================================================
    # PART 13
    # =====================================================================
    story.append(P("PART 13 — Inference / Generation", st["PartTitle"]))
    story.append(hr())

    story.append(P("13.1 Autoregressive loop", st["CourseH2"]))
    story.append(mono("""
Encode source once → Memory M

y = [<BOS>]
loop:
  decoder(y, M) with causal mask
  take logits at last position
  choose next token:
     greedy: argmax
     or sampling / beam search
  append token to y
  stop at <EOS> or max length

Example:
  y = [<BOS>]
  → predicts J'aime
  y = [<BOS>, J'aime]
  → predicts les
  y = [<BOS>, J'aime, les]
  → predicts chats
  y = [<BOS>, J'aime, les, chats]
  → predicts <EOS> → stop
""", st))

    story.append(P("13.2 Training vs inference", st["CourseH2"]))
    story.append(P(
        "Training uses teacher forcing (parallel over target length). "
        "Inference is sequential token-by-token — a major speed cost of autoregressive decoding. "
        "Exposure bias: train sees gold prefixes; inference sees its own prefixes — a known issue.",
        st["CourseKey"]
    ))

    story.append(P("13.3 Greedy vs beam search", st["CourseH2"]))
    story.extend(bullets([
        "<b>Greedy:</b> always pick top-1; fast; can commit early mistakes.",
        "<b>Beam search:</b> keep top-B partial hypotheses; often better BLEU; slower; paper reports beam results.",
    ], st))
    story.append(P(
        "Paper connection: §5–6 mention beam search settings used for BLEU numbers.",
        st["CourseCallout"]
    ))

    story.append(P("13.4 Step-by-step greedy decode for the running example", st["CourseH2"]))
    story.append(mono("""
M = Encode("I love cats")

step1: y=[BOS]           → probs → pick J'aime
step2: y=[BOS,J'aime]    → probs → pick les
step3: y=[BOS,J'aime,les]→ probs → pick chats
step4: y=[...,chats]     → probs → pick EOS → stop

At each step, masked self-attn only sees the growing prefix;
cross-attn always sees full M.
""", st))
    story.append(P("13.5 Why caching matters (implementation note)", st["CourseH2"]))
    story.append(P(
        "Naive inference recomputes attention for the whole prefix every step. Production systems cache "
        "past K/V (KV cache). Conceptually identical results; engineering speedup. The 2017 paper does not "
        "require you to invent KV caching to understand the model.",
        st["CourseBody"]
    ))
    story.append(PageBreak())

    # =====================================================================
    # PART 14
    # =====================================================================
    story.append(P("PART 14 — The Paper’s Equations (Decoded)", st["PartTitle"]))
    story.append(hr())

    story.append(P("14.1 Scaled Dot-Product Attention", st["CourseH2"]))
    story.append(P("Attention(Q,K,V)=softmax(QKᵀ/√d_k)V", st["CourseEq"]))
    story.append(P(
        "Symbols/shapes/intuition/computation: Part 3. Location: core of every attention head. "
        "Why: content-based soft lookup that is GPU-friendly (matmul).",
        st["CourseBody"]
    ))

    story.append(P("14.2 Multi-Head", st["CourseH2"]))
    story.append(P(
        "MultiHead(Q,K,V)=Concat(head_i)W^O with head_i=Attention(QW_i^Q, KW_i^K, VW_i^V)",
        st["CourseEq"]
    ))
    story.append(P(
        "Location: encoder self-attn, decoder masked self-attn, decoder cross-attn. "
        "Why: multiple subspaces / relation types.",
        st["CourseBody"]
    ))

    story.append(P("14.3 FFN", st["CourseH2"]))
    story.append(P("FFN(x)=max(0,xW1+b1)W2+b2", st["CourseEq"]))
    story.append(P("Location: after attention sublayer in every encoder/decoder layer. Why: per-position nonlinear capacity.", st["CourseBody"]))

    story.append(P("14.4 Positional Encoding", st["CourseH2"]))
    story.append(P("PE(pos,2i)=sin(pos/10000^(2i/d_model)); PE(pos,2i+1)=cos(...)", st["CourseEq"]))
    story.append(P("Location: added to token embeddings at encoder and decoder bottoms. Why: inject order.", st["CourseBody"]))

    story.append(P("14.5 Add & Norm (Post-LN)", st["CourseH2"]))
    story.append(P("LayerNorm(x + Sublayer(x))", st["CourseEq"]))
    story.append(P(
        "Location: around every sublayer in Fig. 1. Why: deep residual training stability. "
        "Contrast: modern Pre-LN is Sublayer(LayerNorm(x)) + x.",
        st["CourseBody"]
    ))

    story.append(P("14.6 Equation → module map", st["CourseH2"]))
    story.append(simple_table([
        ["<b>Equation</b>", "<b>Module</b>", "<b>Course part</b>"],
        ["Attention(...)", "ScaledDotProductAttention", "Part 3"],
        ["MultiHead(...)", "MultiHeadAttention", "Part 5"],
        ["FFN(...)", "Positionwise FFN", "Part 7"],
        ["PE(...)", "Sinusoidal PE", "Part 6"],
        ["LayerNorm(x+...)", "AddNorm Post-LN", "Part 8"],
    ], [2.0*inch, 2.2*inch, 1.8*inch], st))
    story.append(PageBreak())

    # =====================================================================
    # PART 15
    # =====================================================================
    story.append(P("PART 15 — Original 2017 Architecture Specs", st["PartTitle"]))
    story.append(hr())

    story.append(P("15.1 ARCHITECTURE (what the machine is)", st["CourseH2"]))
    story.extend(bullets([
        "N = 6 encoder layers, N = 6 decoder layers",
        "d_model = 512 (Base); Big uses 1024",
        "h = 8 heads (Base) → d_k = d_v = 64",
        "d_ff = 2048 (Base)",
        "sinusoidal positional encoding",
        "learned embeddings; residual + LayerNorm in <b>Post-LN</b> order",
        "shared embedding weights with pre-softmax linear (weight tying)",
        "no recurrence, no convolution in the backbone",
    ], st))

    story.append(P("15.2 TRAINING PROCEDURE", st["CourseH2"]))
    story.extend(bullets([
        "WMT 2014 EN–DE and EN–FR translation",
        "next-token cross-entropy with teacher forcing",
        "Adam optimizer with custom LR schedule (warmup then decay)",
        "label smoothing ε_ls = 0.1",
    ], st))

    story.append(P("15.3 IMPLEMENTATION DETAILS", st["CourseH2"]))
    story.extend(bullets([
        "dropout P_drop = 0.1",
        "batching by approximate token counts",
        "beam search at inference for reported BLEU",
        "checkpoint averaging sometimes used for reporting",
    ], st))
    story.append(P(
        "Keep these three buckets separate when discussing the paper.",
        st["CourseKey"]
    ))

    story.append(P("15.4 Base vs Big (high level)", st["CourseH2"]))
    story.append(mono("""
Base: d_model=512, h=8,  d_ff=2048, dropout=0.1
Big:  d_model=1024,h=16, d_ff=4096, dropout=0.3
Bigger models → better BLEU, more compute.
""", st))
    story.append(PageBreak())

    # =====================================================================
    # PART 16
    # =====================================================================
    story.append(P("PART 16 — Complexity and Why Transformers Scale", st["PartTitle"]))
    story.append(hr())
    story.append(mono("""
Per layer (conceptual) — paper Table 1 spirit:

                  Complexity/layer     Sequential ops    Max path length
Self-Attention    O(T^2 · d)           O(1)              O(1)
Recurrent         O(T · d^2)           O(T)              O(T)
Convolution       O(k · T · d^2)       O(1)              O(log_k T) or O(T/k)

T=sequence length, d=dimension, k=kernel size.
""", st))
    story.append(P(
        "Transformers won despite O(T²) because: excellent GPU parallelization, short path lengths for long-range "
        "dependencies, and favorable scaling with data/compute. Quadratic cost becomes painful for very long context — "
        "motivating later efficient-attention variants (sparse, linear, FlashAttention engineering, etc.).",
        st["CourseBody"]
    ))
    story.append(P(
        "Key insight: sequential operations (RNN depth in time) hurt wall-clock training more than FLOPs alone suggest.",
        st["CourseKey"]
    ))
    story.append(PageBreak())

    # =====================================================================
    # PART 17
    # =====================================================================
    story.append(P("PART 17 — Reading the Results Section", st["PartTitle"]))
    story.append(hr())
    story.extend(bullets([
        "<b>WMT:</b> standard machine translation benchmarks (news translation).",
        "<b>BLEU:</b> n-gram overlap metric vs references; higher is better (imperfect but standard then).",
        "<b>Baselines:</b> prior RNN/CNN translation systems; compare quality and training cost.",
        "<b>Parameter counts / training time:</b> not only accuracy — efficiency claims matter.",
        "<b>Ablation:</b> remove or alter a piece (heads, PE type, d_k, …) and measure drop — shows which parts matter.",
    ], st))
    story.append(P(
        "Demonstrated ≠ suggested. Demonstrated: numbers on stated tasks. Suggested: broader speculation "
        "(e.g., applicability beyond MT). Read tables carefully before believing headlines.",
        st["CourseWarn"]
    ))
    story.append(P(
        "When you reread §6: ask “what exactly was measured?” and “what was held constant in the ablation?”",
        st["CourseCallout"]
    ))
    story.append(PageBreak())

    # =====================================================================
    # PART 18
    # =====================================================================
    story.append(P("PART 18 — Limitations of the Original Transformer", st["PartTitle"]))
    story.append(hr())
    story.extend(bullets([
        "Quadratic attention memory/compute in T",
        "Long-context difficulty at original design point",
        "Autoregressive decoding latency at inference",
        "Absolute sinusoidal PE is not the end of position modeling",
        "Needs large data/compute to shine",
        "Attention weights ≠ complete interpretability",
        "Teacher forcing / exposure bias",
    ], st))
    story.append(P("Later differences (do not confuse with 2017):", st["CourseH2"]))
    story.extend(bullets([
        "Pre-LN instead of Post-LN",
        "Learned / relative / RoPE positions",
        "Decoder-only GPT-style LMs; encoder-only BERT",
        "Efficient / approximate attention; better kernels",
        "Huge scale, instruction tuning, RLHF — far beyond original MT setting",
    ], st))
    story.append(P(
        "Know these exist so you don’t confuse them with Vaswani 2017 when reconstructing Fig. 1.",
        st["CourseKey"]
    ))
    story.append(PageBreak())

    # =====================================================================
    # PART 19 — EXPANDED PYTORCH
    # =====================================================================
    story.append(P("PART 19 — Implement a Miniature Transformer (PyTorch)", st["PartTitle"]))
    story.append(hr())
    story.append(P(
        "Below is a compact educational implementation. Every class maps to a paper component. "
        "Shapes assume batch first: (B, T, d). This uses <b>Post-LN</b> to match 2017.",
        st["CourseCallout"]
    ))

    story.append(P("19.1 Scaled dot-product + multi-head", st["CourseH2"]))
    story.append(mono("""
import math
import torch
import torch.nn as nn
import torch.nn.functional as F

class ScaledDotProductAttention(nn.Module):
    def forward(self, Q, K, V, mask=None):
        # Q,K,V: (B, h, T, d_k)
        d_k = Q.size(-1)
        scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(d_k)
        if mask is not None:
            scores = scores.masked_fill(mask == 0, -1e9)
        attn = F.softmax(scores, dim=-1)          # (B,h,T_q,T_k)
        return torch.matmul(attn, V), attn        # (B,h,T_q,d_k)

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, h):
        super().__init__()
        assert d_model % h == 0
        self.d_k = d_model // h
        self.h = h
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)
        self.attn = ScaledDotProductAttention()

    def split_heads(self, x):
        # (B,T,d) -> (B,h,T,d_k)
        B, T, _ = x.shape
        return x.view(B, T, self.h, self.d_k).transpose(1, 2)

    def forward(self, query, key, value, mask=None):
        Q = self.split_heads(self.W_q(query))
        K = self.split_heads(self.W_k(key))
        V = self.split_heads(self.W_v(value))
        if mask is not None:
            mask = mask.unsqueeze(1)  # broadcast over heads
        out, weights = self.attn(Q, K, V, mask)
        out = out.transpose(1, 2).contiguous().view(
            query.size(0), query.size(1), -1)
        return self.W_o(out), weights
""", st))

    story.append(P("19.2 FFN, Post-LN AddNorm, sinusoidal PE", st["CourseH2"]))
    story.append(mono("""
class PositionwiseFFN(nn.Module):
    def __init__(self, d_model, d_ff):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(d_model, d_ff), nn.ReLU(), nn.Linear(d_ff, d_model)
        )
    def forward(self, x):
        return self.net(x)

class AddNorm(nn.Module):
    # Post-LN as in 2017 paper: LayerNorm(x + Dropout(sublayer(x)))
    def __init__(self, d_model, dropout=0.1):
        super().__init__()
        self.norm = nn.LayerNorm(d_model)
        self.drop = nn.Dropout(dropout)
    def forward(self, x, sublayer_out):
        return self.norm(x + self.drop(sublayer_out))

class SinusoidalPE(nn.Module):
    def __init__(self, d_model, max_len=5000):
        super().__init__()
        pe = torch.zeros(max_len, d_model)
        pos = torch.arange(0, max_len).unsqueeze(1).float()
        div = torch.exp(torch.arange(0, d_model, 2).float() *
                        (-math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(pos * div)
        pe[:, 1::2] = torch.cos(pos * div)
        self.register_buffer("pe", pe.unsqueeze(0))  # (1,L,d)
    def forward(self, x):
        return x + self.pe[:, :x.size(1)]
""", st))

    story.append(P("19.3 Encoder and decoder layers", st["CourseH2"]))
    story.append(mono("""
class EncoderLayer(nn.Module):
    def __init__(self, d_model, h, d_ff, dropout=0.1):
        super().__init__()
        self.self_attn = MultiHeadAttention(d_model, h)
        self.ffn = PositionwiseFFN(d_model, d_ff)
        self.an1 = AddNorm(d_model, dropout)
        self.an2 = AddNorm(d_model, dropout)
    def forward(self, x, src_mask=None):
        a, _ = self.self_attn(x, x, x, src_mask)
        x = self.an1(x, a)
        return self.an2(x, self.ffn(x))

class DecoderLayer(nn.Module):
    def __init__(self, d_model, h, d_ff, dropout=0.1):
        super().__init__()
        self.self_attn = MultiHeadAttention(d_model, h)
        self.cross_attn = MultiHeadAttention(d_model, h)
        self.ffn = PositionwiseFFN(d_model, d_ff)
        self.an1 = AddNorm(d_model, dropout)
        self.an2 = AddNorm(d_model, dropout)
        self.an3 = AddNorm(d_model, dropout)
    def forward(self, y, memory, tgt_mask=None, memory_mask=None):
        a, _ = self.self_attn(y, y, y, tgt_mask)
        y = self.an1(y, a)
        c, _ = self.cross_attn(y, memory, memory, memory_mask)
        y = self.an2(y, c)
        return self.an3(y, self.ffn(y))

def causal_mask(T, device):
    # 1 = keep, 0 = block
    return torch.tril(torch.ones(1, T, T, device=device))
""", st))

    story.append(P("19.4 Full miniature model skeleton", st["CourseH2"]))
    story.append(mono("""
class MiniTransformer(nn.Module):
    def __init__(self, src_vocab, tgt_vocab, d_model=64, h=4,
                 d_ff=256, N=2, dropout=0.1):
        super().__init__()
        self.d_model = d_model
        self.src_emb = nn.Embedding(src_vocab, d_model)
        self.tgt_emb = nn.Embedding(tgt_vocab, d_model)
        self.pe = SinusoidalPE(d_model)
        self.enc = nn.ModuleList(
            [EncoderLayer(d_model, h, d_ff, dropout) for _ in range(N)])
        self.dec = nn.ModuleList(
            [DecoderLayer(d_model, h, d_ff, dropout) for _ in range(N)])
        self.out = nn.Linear(d_model, tgt_vocab)

    def encode(self, src, src_mask=None):
        x = self.pe(self.src_emb(src) * math.sqrt(self.d_model))
        for layer in self.enc:
            x = layer(x, src_mask)
        return x

    def decode(self, tgt, memory, tgt_mask=None, memory_mask=None):
        y = self.pe(self.tgt_emb(tgt) * math.sqrt(self.d_model))
        for layer in self.dec:
            y = layer(y, memory, tgt_mask, memory_mask)
        return self.out(y)

    def forward(self, src, tgt, src_mask=None, tgt_mask=None):
        memory = self.encode(src, src_mask)
        return self.decode(tgt, memory, tgt_mask, src_mask)

# Train: logits = model(src, tgt_in, tgt_mask=causal_mask(T))
#        loss = cross_entropy(logits.reshape(-1,V), tgt_out.reshape(-1))
# Infer: encode once; append argmax tokens until EOS
""", st))

    story.append(P("19.5 Line-to-equation map", st["CourseH2"]))
    story.extend(bullets([
        "matmul Q Kᵀ → scores; /sqrt → scale; masked_fill → causal/pad; softmax → weights; matmul V → output",
        "view/transpose → multi-head reshape; W_o → W^O",
        "LayerNorm(x+...) → Add & Norm Post-LN",
        "sin/cos buffer → sinusoidal PE; *sqrt(d_model) → paper embedding scale",
    ], st))
    story.append(P(
        "Exercise: change AddNorm to Pre-LN and observe that you have left the 2017 architecture.",
        st["CourseWarn"]
    ))

    story.append(P("19.6 Tiny train / infer sketch", st["CourseH2"]))
    story.append(mono("""
model = MiniTransformer(src_vocab=50, tgt_vocab=50, d_model=64, h=4, N=2)
opt = torch.optim.Adam(model.parameters(), lr=1e-3, betas=(0.9,0.98), eps=1e-9)

# --- one training step ---
src = torch.tensor([[1,2,3]])            # I love cats
tgt_in = torch.tensor([[4,5,6,7]])       # BOS J'aime les chats
tgt_out = torch.tensor([[5,6,7,8]])      # J'aime les chats EOS
T = tgt_in.size(1)
mask = causal_mask(T, src.device)
logits = model(src, tgt_in, tgt_mask=mask)   # (1,4,50)
loss = F.cross_entropy(logits.reshape(-1,50), tgt_out.reshape(-1))
loss.backward(); opt.step(); opt.zero_grad()

# --- greedy inference ---
memory = model.encode(src)
ys = torch.tensor([[4]])  # BOS
for _ in range(10):
    m = causal_mask(ys.size(1), src.device)
    logit = model.decode(ys, memory, tgt_mask=m)
    next_id = logit[:, -1, :].argmax(-1, keepdim=True)
    ys = torch.cat([ys, next_id], dim=1)
    if next_id.item() == 8:  # EOS
        break
""", st))

    story.append(P("19.7 Debugging shapes (common errors)", st["CourseH2"]))
    story.extend(bullets([
        "Forgot transpose for scores → matmul shape error on last two dims",
        "Causal mask wrong broadcast → attending to future (train/test mismatch)",
        "Cross-attn called as self-attn (K=V=decoder) → no source reading",
        "Pre-LN accidentally → still runs, but not paper-faithful",
        "Forgot *sqrt(d_model) on embeddings → scale mismatch with PE",
    ], st))

    story.append(P("19.8 Mapping classes → paper figure boxes", st["CourseH2"]))
    story.append(mono("""
SinusoidalPE + Embedding     → bottom of Fig.1
EncoderLayer.self_attn       → encoder Multi-Head Attention
EncoderLayer.ffn             → Feed Forward
AddNorm                      → Add & Norm (Post-LN)
DecoderLayer.self_attn       → masked Multi-Head Attention
DecoderLayer.cross_attn      → encoder-decoder Multi-Head Attention
MiniTransformer.out          → final Linear (+ softmax outside / in loss)
""", st))

    story.append(PageBreak())

    # =====================================================================
    # PART 20 — QUIZ + ANSWER KEY
    # =====================================================================
    story.append(P("SYNTHESIS — Putting the Whole Machine Together", st["PartTitle"]))
    story.append(hr())
    story.append(P(
        "Before the quiz, lock the global story. The Transformer is not a pile of unrelated tricks; "
        "each piece repairs a specific failure mode of “just multiply embeddings.”",
        st["CourseCallout"]
    ))
    story.append(P("S.1 One-page architecture contract", st["CourseH2"]))
    story.append(mono("""
INPUT: token ids (source) and token ids (target, shifted)
REPRESENT: Embedding * sqrt(d_model) + sinusoidal PE
ENCODE:  N x (SelfAttn + PostLN + FFN + PostLN)
DECODE:  N x (MaskedSelfAttn + PostLN + CrossAttn + PostLN + FFN + PostLN)
PREDICT: Linear to |V|; softmax in loss / decoding
TRAIN:   teacher forcing + causal mask + CE (+ label smoothing) + Adam schedule
INFER:   encode once; autoregressive decode (greedy/beam)
""", st))
    story.append(P("S.2 Running example end-to-end checklist", st["CourseH2"]))
    story.extend(bullets([
        "English “I love cats” becomes contextual memory M via encoder self-attention.",
        "French generation starts at &lt;BOS&gt;; masked self-attn keeps it causal.",
        "Cross-attn grounds “chats” in “cats” (and neighbors).",
        "Without PE, order collapses; without mask, training cheats; without cross-attn, no translation.",
    ], st))
    story.append(P("S.3 Post-LN loyalty check", st["CourseH2"]))
    story.append(P(
        "If your mental diagram shows LayerNorm before attention inside the residual branch as the default, "
        "you are thinking of modern Pre-LN. For Vaswani 2017, rewrite it as Add then Norm.",
        st["CourseWarn"]
    ))
    story.append(P("S.4 Equation → failure mode table", st["CourseH2"]))
    story.append(simple_table([
        ["<b>If removed</b>", "<b>Failure</b>"],
        ["√d_k scale", "Softmax saturation / weak grads"],
        ["Multi-head", "One pattern must do all jobs"],
        ["PE", "Bag-of-tokens mixer"],
        ["FFN nonlinearity", "Depth collapses toward linear"],
        ["Residual", "Deep optimization failure"],
        ["Causal mask", "Train/infer mismatch"],
        ["Cross-attn", "No source conditioning"],
    ], [2.2*inch, 4.0*inch], st))
    story.append(PageBreak())

    story.append(P("PART 20 — Final Master Understanding (Quiz)", st["PartTitle"]))
    story.append(hr())
    story.append(P(
        "Attempt answers yourself before checking the answer key. Write shapes when relevant.",
        st["CourseCallout"]
    ))

    story.append(P("Questions", st["CourseH2"]))
    qs = [
        ("Level 1", "What is attention, in one precise sentence? What tensors are Q, K, V?"),
        ("Level 2", "Why do we need separate Q, K, and V instead of using X three times without projections?"),
        ("Level 3", "Why scale QKᵀ by √d_k? What goes wrong for large d_k without scaling?"),
        ("Level 4", "Why multi-head attention? What are the shapes for Base (d_model=512, h=8)?"),
        ("Level 5", "Why positional encoding? Compute PE(pos=1, dim=0) and PE(pos=1, dim=1) for d_model=4."),
        ("Level 6", "Why residual connections? Write Post-LN vs Pre-LN formulas and say which is 2017."),
        ("Level 7", "Why masked self-attention? Draw the 4×4 causal mask for “&lt;BOS&gt; J’aime les chats”."),
        ("Level 8", "How does cross-attention work for translating “cats” → “chats”? Who provides Q vs K/V?"),
        ("Level 9", "Trace one source token and one target position through the full Transformer "
                    "(embeddings → encoder → decoder → logits), listing shapes with d_model=512, T_src=3, T_tgt=4."),
        ("Level 10", "Design a Transformer variant for a new problem (e.g., long-document QA or decoder-only LM). "
                     "What would you change and why? What would you keep?"),
    ]
    for lvl, q in qs:
        story.append(P(f"<b>{lvl}:</b> {q}", st["CourseBody"]))

    story.append(PageBreak())
    story.append(P("Answer key (use only after attempting)", st["CourseH2"]))
    story.append(hr())

    story.append(P(
        "<b>A1:</b> Attention is a soft weighted lookup: compare each query to all keys (scaled dots), "
        "softmax to weights, mix values. Q asks; K is address; V is content. Shapes: Q (T_q×d_k), "
        "K (T_k×d_k), V (T_k×d_v), output (T_q×d_v).",
        st["CourseBody"]
    ))
    story.append(P(
        "<b>A2:</b> Learned projections let matching (Q/K space) differ from content (V space) and differ "
        "across heads. Using raw X without W_Q/W_K/W_V removes the ability to specialize subspaces.",
        st["CourseBody"]
    ))
    story.append(P(
        "<b>A3:</b> Dot products grow in magnitude with d_k → softmax saturates toward one-hot → tiny gradients. "
        "Dividing by √d_k keeps score variance ~O(1).",
        st["CourseBody"]
    ))
    story.append(P(
        "<b>A4:</b> Multiple subspaces/relation types in parallel; concat + W^O mixes them. "
        "Base: d_k=d_v=64; each head (T×64); concat (T×512); out (T×512).",
        st["CourseBody"]
    ))
    story.append(P(
        "<b>A5:</b> Without PE, attention is order-agnostic (permutation equivariant). "
        "For d_model=4, i=0 denom=1: PE(1,0)=sin(1)≈0.8415; PE(1,1)=cos(1)≈0.5403.",
        st["CourseBody"]
    ))
    story.append(P(
        "<b>A6:</b> Residuals ease deep optimization (learn refinements). "
        "2017 Post-LN: LayerNorm(x+Sublayer(x)). Pre-LN: x+Sublayer(LayerNorm(x)).",
        st["CourseBody"]
    ))
    story.append(P(
        "<b>A7:</b> Prevents attending to future target tokens so training matches autoregressive generation. "
        "Lower-triangular allowed region; strict upper triangle is −inf before softmax.",
        st["CourseBody"]
    ))
    story.append(P(
        "<b>A8:</b> Decoder queries attend to encoder keys/values. For “chats”, Q comes from decoder state "
        "at that position; K/V from contextualized source — ideally high weight on “cats”.",
        st["CourseBody"]
    ))
    story.append(P(
        "<b>A9:</b> ids→Emb×√512+PE → (3×512) encoder self-attn/FFN×6 → M (3×512); "
        "tgt (4×512) masked SA → cross-attn to M (scores 4×3) → FFN×6 → Linear to |V| → softmax. "
        "Loss on each of 4 positions.",
        st["CourseBody"]
    ))
    story.append(P(
        "<b>A10 (example):</b> Decoder-only LM: drop encoder &amp; cross-attn; keep masked self-attn+FFN+PE. "
        "Long-doc QA: keep encoder–decoder or encoder-only with span head; maybe sparse attention for long T; "
        "justify each change against quadratic cost / task structure. Keep residual+norm+attention core.",
        st["CourseBody"]
    ))


    story.append(P("Bonus drills (Part 20 continued)", st["CourseH2"]))
    story.extend(bullets([
        "<b>B1:</b> Recompute Part 3’s A V with a different V; show only the readout changes.",
        "<b>B2:</b> Write causal masks for T=5 by hand.",
        "<b>B3:</b> For d_model=512, h=8, list every matrix multiply in one encoder layer.",
        "<b>B4:</b> Explain why teacher forcing needs a mask even though gold targets are available.",
        "<b>B5:</b> Contrast Post-LN vs Pre-LN on a napkin diagram of one block.",
    ], st))
    story.append(P("Bonus short answers", st["CourseH3"]))
    story.extend(bullets([
        "<b>B1:</b> Scores/weights unchanged if Q,K fixed; output rows change with V.",
        "<b>B2:</b> Lower-triangular ones / upper −inf.",
        "<b>B3:</b> Q,K,V projections; QKᵀ; AV; W_O; FFN W1; FFN W2 (plus norms).",
        "<b>B4:</b> Gold future tokens exist in the tensor — mask stops leakage so train matches generate.",
        "<b>B5:</b> Post: sublayer→add→norm; Pre: norm→sublayer→add.",
    ], st))

    story.append(Spacer(1, 10))
    story.append(P("Final mental model (inevitable architecture)", st["CourseH2"]))
    story.append(mono("""
Need seq2seq → encoder/decoder
Need parallel long-range mixing → self-attention
Need multi relations → multi-head
Need order → positional encoding
Need per-token nonlinear think → FFN
Need deep stacks to train → residual + norm (Post-LN in 2017)
Need left-to-right generation → causal mask
Need source info in decoder → cross-attention
Need probabilities → linear + softmax

If someone shows you Fig.1 or Attention(Q,K,V)=softmax(QKᵀ/√d_k)V,
you should now rebuild the system from first principles.
""", st))
    story.append(P(
        "You are ready to reread Vaswani et al. 2017 — this time as an architect, not as a tourist.",
        st["CourseKey"]
    ))

    # Build PDF
    os.makedirs(os.path.dirname(OUT_ARTIFACT), exist_ok=True)
    os.makedirs(os.path.dirname(OUT_WORKSPACE), exist_ok=True)
    doc = SimpleDocTemplate(
        OUT_ARTIFACT,
        pagesize=letter,
        rightMargin=0.7 * inch,
        leftMargin=0.7 * inch,
        topMargin=0.65 * inch,
        bottomMargin=0.65 * inch,
        title="Transformer Complete Course — Attention Is All You Need",
        author="Cursor Transformer Course",
    )
    doc.build(story, onFirstPage=add_header_footer, onLaterPages=add_header_footer)
    shutil.copy(OUT_ARTIFACT, OUT_WORKSPACE)
    print("Wrote", OUT_ARTIFACT)
    print("Wrote", OUT_WORKSPACE)


if __name__ == "__main__":
    build()
