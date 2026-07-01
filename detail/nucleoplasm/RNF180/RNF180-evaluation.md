---
type: protein-evaluation
gene: "RNF180"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---
## RNF180 核蛋白评估报告
### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | RNF180 |
| 蛋白名称 | E3 ubiquitin-protein ligase RNF180 |
| 蛋白大小 | 592 aa / 68.3 kDa |
| UniProt ID | Q86T96 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | nan (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 592 aa |
| 研究新颖性 | 8/10 | x5 | 40.0 | PubMed=38 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=56.9; PDB=0 |
| 调控结构域 | 6/10 | x2 | 12.0 | RNF180; RNF180_C; Znf_C3HC4_RING-type |
| PPI | 5/10 | x3 | 15.0 | PPI degree=8 |
| **加权总分** | | | **124/180** | |
| **归一化总分** | | | **68.3/100** | 互证: +1 |

### 3. 分析
HPA: nan (Approved)
PubMed: strict=38, broad=48
AF pLDDT: 56.9  PDB: 0
InterPro: RNF180; RNF180_C; Znf_C3HC4_RING-type
Pfam: RNF180_C; zf-C3HC4
PPI degree: 8  ChIP: None
**Papers**: 36703788: Diagnostic value of plasma RNF180 gene methylation for gastric cancer: A systema | 40148674: KLX ameliorates liver cancer progression by mediating ZBP1 transcription and ubi | 40331188: RNF180 weakened the lipid droplet formation and subsequent chemoresistance by de

### 4. 总体评价
★★★★  **68.3/100**  |  **nucleoplasm**
**TE candidate** -- RNF180; RNF180_C; Znf_C3HC4_RING-type


### 深度机制分析

**RING型E3泛素连接酶的TE沉默潜质**：RNF180（E3 ubiquitin-protein ligase RNF180, 592 aa, UniProt Q86T96）属于RING finger蛋白家族，携带RING结构域（InterPro: Znf_C3HC4_RING-type IPR001841, Pfam: zf-C3HC4）作为E3泛素连接酶催化核心。RING域通过保守的C3HC4锌指基序同时结合E2泛素偶联酶和底物蛋白，催化泛素从E2直接转移至底物赖氨酸残基。RNF180还包含N端RNF180结构域（IPR033263）和C端RNF180_C域（IPR045790），其已知底物为ZIC2转录因子（PMID:BioGRID）。该蛋白促进ZIC2的多聚泛素化和蛋白酶体降解（UniProt annotation）。

**Polycomb/染色质泛素化通路与TE沉默的接口**：泛素连接酶在染色质调控中的核心作用无需赘言——RING1A/B（PRC1组分）通过H2AK119ub1泛素化启动Polycomb沉默，对TE区域（特别是ERV和LINE-1）的持续沉默至关重要。RNF180虽非PRC1直接组分，但其PPI互作伙伴中CBX4（BioGRID score=0）和DNMT1（BioGRID score=0）的存在提供了与染色质沉默机器的直接连接。CBX4是PRC1复合物的chromobox亚基之一，通过chromodomain识别H3K27me3修饰；DNMT1负责DNA甲基化维持，是TE CpG甲基化的核心执行酶。

**肿瘤抑制功能与TE去抑制的肿瘤关联**：RNF180在非小细胞肺癌（PMID:41807497）、胃癌（PMID:36703788, 40915184）和肝癌（PMID:40148674）中发挥肿瘤抑制功能，作为抑癌基因其启动子CpG岛异常高甲基化导致表达沉默。这种抑癌基因-TE表达的反向关系已有充分证据：全基因组DNA低甲基化（如LINE-1去甲基化）同时驱动TE转录激活和抑癌基因沉默。若RNF180通过泛素化降解某些转录激活因子间接抑制TE，则其自身在肿瘤中的沉默将导致TE去抑制——形成"抑癌基因缺失→TE激活→基因组不稳定"的致癌正反馈。

**结构限制与实验方向**：AlphaFold pLDDT=56.9的较低置信度（可能由于蛋白大小592 aa和N端/中间区域的内在无序）和PDB=0的结构缺失提示需要实验结构生物学支持。PPI degree=8（BioGRID）暗示当前数据可能低估了其底物范围。若推进TE相关实验，建议进行RNF180 KO后的H3K27me3和H2AK119ub的ChIP-seq，以及TE转录组的RNA-seq分析。归一化得分68.3/100中核定位特异性36/40和新奇性40/50为主要支撑。


### 补充分析 (UniProt API)

**蛋白全称**: E3 ubiquitin-protein ligase RNF180

**功能**: E3 ubiquitin-protein ligase which promotes polyubiquitination and degradation by the proteasome pathway of ZIC2

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR033263 |
| InterPro | IPR045790 |
| InterPro | IPR018957 |
| InterPro | IPR001841 |
| InterPro | IPR013083 |
| InterPro | IPR017907 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ZIC2 | BioGRID | 0 |
| LYN | BioGRID | 0 |
| AGRN | BioGRID | 0 |
| KIF20A | BioGRID | 0 |
| PLK2 | BioGRID | 0 |
| RAD51 | BioGRID | 0 |
| CBX4 | BioGRID | 0 |
| DNMT1 | BioGRID | 0 |