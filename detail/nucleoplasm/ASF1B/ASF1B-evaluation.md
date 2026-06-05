---
type: protein-evaluation
gene: "ASF1B"
date: 2026-06-01
tags: [protein-scout, nucleoplasm, evaluation]
status: scored
---

## ASF1B 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | ASF1B |
| 蛋白全名 | Histone chaperone ASF1B |
| 蛋白大小 | 202 aa / 22.4 kDa |
| UniProt ID | Q9NVP2 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | x4 | 28.0 | UniProt Nucleus; Cytosol, HPA Nucleoplasm |
| 蛋白大小 | 10/10 | x1 | 10.0 | 202 aa, 22.4 kDa，极小 |
| 研究新颖性 | 2/10 | x5 | 10.0 | PubMed strict=81 (≤100 区间) |
| 三维结构 | 8/10 | x3 | 24.0 | PDB 4 entries (5BNX/5BO0/7V1M/7VCQ), AF pLDDT 84.6, >90=75.2% |
| 调控结构域 | 9/10 | x2 | 18.0 | Histone chaperone ASF1 domain，直接结合 H3/H4 二聚体 |
| PPI 网络 | 8/10 | x3 | 24.0 | STRING NASP 0.999, H3-3B 0.998, MCM2 0.996, CHAF1B 0.993, TLK2 0.981；IntAct 15+ 条 |
| **加权总分** | | | **114/180**** | |
| 互证加分 | | | +0.0 | |
| **归一化总分 (÷1.83)** | | | **62.3/100**** | |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt Subcellular Location | Nucleus (ECO:0000269); Cytoplasm, cytosol (ECO:0000269) | 高（实验证据） |
| GO-CC | chromatin (IDA:UniProtKB), nucleoplasm (IDA:HPA), nucleus (IBA:GO_Central), cytosol (IEA) | 高 |
| HPA IF | Nucleoplasm (Enhanced 可靠性) | 高 |

**HPA IF 状态**: IF available -- HPA 可靠性 Enhanced，定位 Nucleoplasm（纯核质）。

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ASF1B/IF_images/ASF1B_IF_red_green.jpg]]

**结论**: ASF1B 是组蛋白伴侣，在核质和胞质间穿梭，核质为主要功能定位。HPA Enhanced 可靠性纯 Nucleoplasm 定位，与组蛋白 H3/H4 的核输入和染色质组装功能一致。

#### 3.2 结构与数据源
| 指标 | 数值 |
|---|---|
| AlphaFold | AF-Q9NVP2-F1 |
| 平均 pLDDT | 84.6 |
| pLDDT >90 | 75.2% |
| pLDDT 70-90 | 1.0% |
| pLDDT <50 | 17.3% |
| PDB | 4 entries (5BNX 2.31A, 5BO0 2.91A, 7V1M 2.83A, 7VCQ 3.00A) -- 与 CDAN1 和组蛋白伴侣复合体共解析 |

AlphaFold pLDDT 84.6，>90 区 75.2%，核心 ASF1 域折叠极好。PDB 4 个结构均为与 CDAN1 等伴侣蛋白的共结晶。N 端 1-158 aa 区结构明确，C 端 ~40 aa 含无序区。

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ASF1B/ASF1B-PAE.png]]

| InterPro | Pfam |
|---|---|
| IPR006818 (ASF1-like histone chaperone), IPR036747 (ASF1-like superfamily) | PF04729 (ASF1_hist_chap) |

**染色质调控潜力**: ASF1B 是复制依赖性染色质组装的核心组蛋白伴侣。直接结合新合成的 H3-H4 二聚体（H3K9me1 + H4K5K12ac 标记），与 CAF-1 协同完成 DNA 复制偶联的核小体组装。TLK1/TLK2 磷酸化 ASF1B 调控其活性。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict (Title/Abstract) | 81 |
| PubMed broad | 146 |
| 别名 | 无 |

关键文献：
- PMID:40091041: "Mechanism of ASF1 engagement by CDAN1." (Nat Commun, 2025) -- ASF1 结构机制
- PMID:38498025: "The TLK-ASF1 histone chaperone pathway plays a critical role in IL-1beta-mediated AML progression." (Blood, 2024)
- PMID:26527279: ASF1B 识别 H3K9me1 和 H4K5K12ac 修饰的新合成组蛋白
- PMID:38537775: "Activation of the FOXM1/ASF1B/PRDX3 axis confers hyperproliferative and antioxidative stress reactivity to gastric cancer." (Cancer Lett, 2024)
- PMID:36416310: "Anti-silencing function 1B promotes the progression of pancreatic cancer by activating c-Myc." (Int J Oncol, 2023)

#### 3.4 PPI 网络（三源综合）
| Partner | Source | Score/Evidence | Relevance |
|---|---|---|---|
| NASP | STRING | 0.999 (exp 0.995) | 组蛋白伴侣 |
| H3-3B | STRING | 0.998 (exp 0.987) | 组蛋白 H3.3 变体 |
| MCM2 | STRING | 0.996 (exp 0.983) | DNA 复制解旋酶 |
| CHAF1B | STRING | 0.993 (exp 0.970) | CAF-1 复合体（复制偶联染色质组装） |
| H4C6 | STRING | 0.993 (exp 0.988) | 组蛋白 H4 |
| TLK2 | STRING | 0.981 (exp 0.875) | 磷酸化激酶 |
| CDAN1 | IntAct | coIP (PMID:17353931) | ASF1 调控因子 |
| TLK1 | IntAct | coIP (PMID:17353931) | 磷酸化激酶 |
| CHAF1A | IntAct | coIP (PMID:17353931) | CAF-1 大亚基 |
| CDAN1 | UniProt | 7 experiments | Codanin-1 |
| TLK2 | UniProt | 8 experiments | Tousled-like kinase 2 |

ASF1B 的 PPI 网络高度集中于组蛋白伴侣/染色质组装体系。NASP、H3/H4 组蛋白、MCM2、CAF-1 (CHAF1A/B) 构成复制偶联染色质组装的核心网络。TLK1/TLK2 通过磷酸化调控 ASF1B。CDAN1 是 ASF1 的抑制因子。UniProt 记录 13 条 curated 互作。

### 4. 总体评价
ASF1B 是核心组蛋白伴侣，与 CAF-1 协同完成复制偶联核小体组装。主要劣势是 PubMed 81 篇（新颖性仅 2/10）。优势包括：极小蛋白（202 aa）、HPA Enhanced 纯核质定位、4 个 PDB 结构（与 CDAN1 复合体）、ASF1 域直接结合 H3/H4、PPI 网络以组蛋白伴侣体系为核心（CAF-1/TLK/CDAN1）。是染色质组装领域的关键靶点，但需注意 ASF1A 的高度同源性（需区分功能）。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NVP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NVP2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ASF1B
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105011-ASF1B

HPA IF 图像已本地嵌入。



**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ASF1B/ASF1B-PAE.png]]

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NVP2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
