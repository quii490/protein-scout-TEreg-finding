---
type: protein-evaluation
gene: "FUNDC2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## FUNDC2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | FUNDC2 |
| 蛋白名称 | FUN14 domain-containing protein 2 |
| 蛋白大小 | 189 aa / 20.7 kDa |
| UniProt ID | Q9BWH2 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 📏 蛋白大小 | 7/10 | ×1 | 7.0 | 189 aa |
| 🆕 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed=18 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=65.9; PDB=0 |
| 🧬 调控结构域 | 4/10 | ×2 | 8.0 | FUN14 |
| 🔗 PPI | 6/10 | ×3 | 18.0 | PPI degree=96 |
| **加权总分** | | | **113/180** | |
| **归一化总分 (÷1.83)** | | | **62.8/100** | 互证: +2 |

### 3. 详细分析

| 项目 | 详情 |
|---|---|
| HPA | nan (nan) |
| PubMed | strict=18, broad=24 |
| AlphaFold | pLDDT=65.9 |
| PDB | 0 entries |
| InterPro | FUN14 |
| Pfam | FUN14 |
| PPI | combined degree=96 |
| ChIP | None |

### 4. 总体评价
⭐⭐⭐⭐
**62.8/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: FUN14 domain-containing protein 2

**功能**: Binds directly and specifically 1,2-Diacyl-sn-glycero-3-phospho-(1'-myo-inositol-3',4',5'-bisphosphate) (PIP3) leading to the recruitment of PIP3 to mitochondria and may play a role in the regulation of the platelet activation via AKT/GSK3B/cGMP signaling pathways (PubMed:29786068). May act as transcription factor that regulates SREBP1 (isoform SREBP-1C) expression in order to modulate triglyceride (TG) homeostasis in hepatocytes (PubMed:25855506, PubMed:29187281)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR007014 |
| Pfam | PF04930 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。


### 深度机制分析

FUNDC2的核心结构域为FUN14结构域（PF04930, IPR007014），该结构域最早在线虫和哺乳动物的FUN14/BNIP3/NIX蛋白家族中被注释，主要定位于线粒体外膜，参与线粒体自噬受体（mitophagy receptor）的调控。典型同源蛋白FUNDC1已被证实为低氧条件下介导线粒体自噬的关键受体，通过其LIR（LC3-interacting region）模体直接与自噬体蛋白LC3结合（PMID:24746696）。FUNDC2与FUNDC1共享FUN14结构域，但其分子功能方向出现重要分岔：UniProt已将其注释为PIP3结合蛋白（PMID:29786068），提示其可能具备磷脂感应功能，而更引人注目的是来自PMID:25855506和29187281的报道——FUNDC2可能作为转录因子直接调控SREBP1（isoform SREBP-1C）的表达，从而调控肝细胞的甘油三酯稳态。这一功能注释极为非典型：一个含线粒体外膜结构域的蛋白为何能进入核内执行转录调控？这是兼职蛋白（moonlighting）的又一典型范例。

从结构分析角度，FUNDC2的AlphaFold pLDDT仅为65.9，远低于可靠结构预测的阈值（通常pLDDT>70视为有序区域），意味着该蛋白整体存在显著的构象柔性或内在无序区域。189 aa的小尺寸（20.7 kDa）进一步限制了其可能包含的独立折叠结构域数量。低置信度结构使得从原子层面对FUN14结构域进行机制推断变得困难——我们无法可靠判断PIP3结合口袋的位置和构象，也无法预测是否存在隐性的DNA结合界面。不过，小蛋白的构象柔性恰好在转录因子中并不少见：许多转录因子的激活域（transactivation domain）本身就是内在无序的，在结合DNA或伙伴蛋白后才发生折叠（induced folding）。

PPI网络方面，FUNDC2的combined degree高达96，表明其在细胞内存在广泛的低亲和力互作。但令人困惑的是，BioGRID中列举的互作伙伴（TP53I3, USP13, ARL15, ASCC2, EIF6, NACA, NSF, RGS1）横跨DNA损伤应答（TP53I3）、去泛素化（USP13）、翻译机器（EIF6, NACA）、囊泡运输（NSF）和GPCR信号（RGS1）等多个不相关的通路。这种高度异质性的PPI图谱与小蛋白的非特异性粘附（sticky protein）特征相符，也可能是双杂交筛选（Y2H）中常见的假阳性富集，缺乏实验验证（BioGRID全部score=0）。相比之下，STRING的96个预测互作虽然覆盖面广，但同样未聚焦于任何特定的转录调控复合体。

综合来看，FUNDC2的TE调控潜力非常有限。其在肝癌细胞中调控SREBP1的报道虽然引人注目，但缺乏后续验证和独立的核定位证据（HPA IF无数据）。FUN14结构域在线粒体自噬中的经典功能与SREBP1转录调控之间的功能鸿沟尚未有任何生化机制解释。若要将FUNDC2纳入TE调控研究管道，最低要求是：(1) 在多个细胞系中通过IF和核质分离Western blot确认核定位；(2) 通过ChIP-seq确定其是否能直接结合基因组TE位点；(3) 验证PIP3结合是否是其核内功能所必需的。在满足这些前置条件之前，FUNDC2的TE调控假说应被视为高度推测性的。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TP53I3 | BioGRID | 0 |
| USP13 | BioGRID | 0 |
| ARL15 | BioGRID | 0 |
| ASCC2 | BioGRID | 0 |
| EIF6 | BioGRID | 0 |
| NACA | BioGRID | 0 |
| NSF | BioGRID | 0 |
| RGS1 | BioGRID | 0 |



### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/FUNDC2
