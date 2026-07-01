---
type: protein-evaluation
gene: "A0A140VJH5"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## A0A140VJH5 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | A0A140VJH5 |
| 蛋白大小 | 744 aa / 82.8 kDa |
| UniProt ID | A0A140VJH5 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 744 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=0 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=52.1; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | DAZ_dom; DAZ_RRM_vert; Nucleotide-bd_a/b_plait_sf |
| PPI | 5/10 | x3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **114/180** | |
| **归一化总分** | | | **62.8/100** | 互证: +1 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=52.1 PDB=0
- InterPro: DAZ_dom; DAZ_RRM_vert; Nucleotide-bd_a/b_plait_sf
- Pfam: Daz; RRM_1
- PPI degree=0 ChIP: None


### 4. 总体评价
**62.8/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

A0A140VJH5含有DAZ结构域（IPR037565, PF13971）和经典RRM（RNA Recognition Motif, IPR035979, PF00076），归属于DAZ（Deleted in Azoospermia）家族的RNA结合蛋白。DAZ家族在哺乳动物中包括DAZ1-DAZ4、DAZL和BOULE等关键生殖细胞调控因子（PMID: 12444072）。DAZ结构域本身由多个重复的RRM单元组成，每个RRM采用βαββαβ折叠，通过RNP1（R/K-G-F/Y-G/A-F-V/I-X-F/Y）和RNP2（I/V-F/Y-I/V-K/R-G/N-L）共识序列识别RNA（PMID: 12165595）。值得注意的是Pfam同时将核苷酸结合α/β平台折叠（Nucleotide-bd_a/b_plait_sf, IPR012677）注释到该蛋白，表明其可能不仅仅结合单链RNA，还可能通过分层β-sheet平台同时结合DNA/RNA复合体如R-loop或DNA-RNA杂交链，这对其在转座子调控中的潜在功能非常关键。744个氨基酸（82.8 kDa）远大于DAZ家族中DAZL的298个氨基酸，提示存在额外的蛋白-蛋白相互作用域。

STRING PPI网络具有显著的Y染色体生殖细胞特异性特征：DAZAP1（Deletion in Azoospermia Associated Protein 1, 445分）、PUM2（pumilio RNA binding protein 2, 977分）、DZIP1（DAZ interacting zinc finger protein 1, 944分）为核心互作伙伴。尤其值得注意的是USP9Y（ubiquitin specific peptidase 9 Y-linked, 663分）和DDX3Y（DEAD-box helicase 3 Y-linked, 661分），两者均为Y染色体编码的生殖细胞必需因子，提示A0A140VJH5可能整合泛素信号和RNA二级结构重塑过程。BPY2家族蛋白（BPY2基本型Y染色体蛋白, 709分）和CDY家族（chromodomain Y, 738分）进一步将互作网锚定在染色质层面，chromodomain读取甲基化组蛋白（H3K9me3、H3K27me3）标签——这是生殖细胞PIWI/piRNA介导TE沉默的标志性标记（PMID: 19182780）。

DAZ家族在精子发生中抑制mRNA翻译的机制已部分阐明：DAZL通过其RRM结合靶mRNA 3'UTR，并与PABP和多聚A聚合酶协作控制mRNA稳定性和翻译效率（PMID: 11752460）。DAZ蛋白的Y染色体局限性（人类DAZ存在于AZFc区域）赋予其在male germline中独特的进化压力下的功能。更为相关的是，DAZAP1被鉴定为pre-mRNA剪接因子，其DAZ结构域偏向识别富含U/A的序列（PMID: 15389235），这恰好与LINE-1元件的3'UTR和Alu元件的高A/U含量重合。

TE调控推测模型：A0A140VJH5作为Y染色体特异性TE监护因子。其DAZ/DAZ_RRM_vert结构域识别LINE-1和SVA元件的3'UTR区域（或在LTR启动子激活后来源于LTR逆转录转座子的转录本）。通过与PUM2合作（PUM2是Pumilio-Nanos翻译抑制复合体的组分，976分），A0A140VJH5可接合到特定TE RNA上并抑制其翻译，防止TE编码的逆转录酶和ORF1p的积累。DDX3Y（661分）作为RNA解旋酶协助A0A140VJH5进入高度结构化的TE RNA区域。一旦结合，CDY1/UPS9Y通过chromodomain读取的H3K9me3和USP9Y的去泛素酶活性可能稳定A0A140VJH5在TE染色质位点的驻留。其pLDDT=52.1提示大量无序区域，这可能用于构象采样以识别多种TE家族的序列变体。这个模型最适合解释为什么A0A140VJH5定位于核质而非细胞质——翻译抑制通常需要穿梭进出核，但该蛋白质的Y染色体限制和Pfam架构偏向核内TE RNA监控。

研究意义：（1）Y染色体生殖细胞TE调控是一个全新领域——目前仅PIWI/piRNA通路被广泛研究；（2）A0A140VJH5可能解释Y染色体微缺失导致的非梗阻性无精子症中TE去抑制现象（PMID: 20534472）；（3）DAZ+DDX3Y+PUM2的RNA结合组合可能代表一种尚未描述的TE RNA转运和降解复合体。优先实验：PAR-CLIP鉴定A0A140VJH5的结合RNA域和特异性TE靶标；精母细胞条件性敲除后进行TE RNA-seq。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| DAZAP1 | STRING | 445 |
| DZIP1 | STRING | 944 |
| PRY | STRING | 600 |
| CDY1 | STRING | 738 |
| PRY2 | STRING | 598 |
| BPY2 | STRING | 709 |
| PUM2 | STRING | 977 |
| USP9Y | STRING | 663 |
| DDX3Y | STRING | 661 |
| BPY2C | STRING | 696 |
| BPY2B | STRING | 696 |
| DAZ2 | STRING | 400 |
| DAZ1 | STRING | 884 |
| CDY2A | STRING | 738 |

### TE 调控评估

该蛋白为核蛋白，但其 TE 调控相关性需进一步实验验证。目前无直接 TE 调控文献支持。


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/A0A140VJH5
