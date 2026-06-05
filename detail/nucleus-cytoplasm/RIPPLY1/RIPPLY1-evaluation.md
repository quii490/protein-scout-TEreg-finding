---
type: protein-evaluation
gene: "RIPPLY1"
date: 2026-06-02
tags: [protein-scout, nucleus-cytoplasm, evaluation]
status: scored
pm: 17
---

## RIPPLY1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | RIPPLY1 (no known aliases) |
| 蛋白全称 | Protein ripply1 |
| 蛋白大小 | 151 aa / 16.4 kDa |
| UniProt ID | Q0D2K3 |
| AlphaFold | AF-Q0D2K3-F1 (v6) |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | **16** | UniProt Nucleus (ECO:0000250 预测); GO nucleus ISS; HPA 无定位数据 |
| 蛋白大小 | 10/10 | ×1 | **10** | 151 aa，理想范围 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed strict=17，≤20 档，极高新颖性 |
| 三维结构 | 3/10 | ×3 | **9** | 无 PDB 结构; AF mean pLDDT 59.8, 仅 2.6% >90 |
| 调控结构域 | 7/10 | ×2 | **14** | TLE/Groucho 结合蛋白，转录共抑制因子功能 |
| PPI 网络 | 7/10 | ×3 | **21** | STRING 14 + IntAct 15; TLE 家族 (TLE1-5) 核心 + HDAC7/THAP1 转录调控 |
| 互证加分 | -- | -- | **+0** | 无显著互证 |
| **加权总分** | | | **120/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleus (ECO:0000250) | 预测级 |
| GO-CC | nucleus (GO:0005634, ISS:UniProtKB) | 预测级 |
| HPA IF | 无定位数据 (page found, no IF localization) | 不可用 |

**HPA IF 状态**: 无可用 IF 定位信息。UniProt 和 GO 均为预测级证据。但 RIPPLY1 作为 TLE/Groucho 共抑制因子的功能提示核定位是合理的。

**结论**: 核定位证据薄弱，仅预测级。但功能上作为转录共抑制因子强烈暗示核功能。

#### 3.2 蛋白大小评估

**评价**: 151 aa (16.4 kDa)，处于理想实验范围下限。小蛋白易于表达纯化。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict (Title/Abstract+gene/protein) | 17 |
| PubMed symbol_only | 21 |
| PubMed broad | 21 |

**关键文献**:
1. Zhangyuan G et al. (2025). "RIPPLY1 suppresses cancer cell stemness via targeting TBX19 in CTNNB1-mutated hepatocellular carcinoma." *Hepatology*. PMID: 40901752
2. Yabe T et al. (2023). "Ripply suppresses Tbx6 to induce dynamic-to-static conversion in somite segmentation." *Nat Commun*. PMID: 37055428
3. Kawamura A et al. (2008). "Activator-to-repressor conversion of T-box transcription factors by the Ripply family." *Mol Cell Biol*. PMID: 18332117
4. Windner SE et al. (2015). "Tbx6, Mesp-b and Ripply1 regulate the onset of skeletal myogenesis in zebrafish." *Development*. PMID: 25725067
5. Yoshizaki H et al. (2015). "Regulation of Ripply1 expression in MDCK organoids." *Biochem Biophys Res Commun*. PMID: 26514726

**评价**: PubMed strict=17，极高新颖性。2025 年 Hepatology 论文首次报道 RIPPLY1 在肝癌中的功能，研究空间极大。传统研究集中于体节发育。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 151 aa |
| PDB 条数 | 0 |
| AlphaFold mean pLDDT | 59.8 |
| pLDDT >90 | 2.6% |
| pLDDT 70-90 | 22.5% |
| pLDDT 50-70 | 45.7% |
| pLDDT <50 | 29.1% |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/RIPPLY1/RIPPLY1-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测。pLDDT 均值 59.8（偏低），仅 2.6% 残基 >90。小蛋白但预测置信度低，可能为部分无序蛋白或需要结合伴侣才稳定折叠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | IPR028127 (Ripply1) |
| Pfam | PF14998 (Ripply1) |

**染色质调控潜力分析**: RIPPLY1 本身结构域注释有限 (Ripply1 家族特有结构域)。但功能上作为 TLE/Groucho 共抑制因子的衔接蛋白，通过将 T-box 转录因子 (TBX6, TBX19) 从激活子转换为抑制子来调控转录。TLE 是经典的转录共抑制因子，与染色质修饰和 HDAC 招募相关。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| TLE1 | anti tag coIP | 28514442 | Transcriptional corepressor | Yes |
| TLE2 | anti tag coIP | 28514442 | Transcriptional corepressor | Yes |
| TLE3 | anti tag coIP | 28514442 | Transcriptional corepressor | Yes |
| TLE4 | anti tag coIP | 28514442 | Transcriptional corepressor | Yes |
| TLE5 | anti tag coIP | 28514442 | Transcriptional corepressor | Yes |
| HDAC7 | two hybrid array | 32296183 | Histone deacetylase | Yes |
| THAP1 | two hybrid array | 32296183 | DNA-binding TF | Yes |
| MED19 | two hybrid array | 32296183 | Mediator complex | Yes |
| PBX4 | two hybrid array | 32296183 | Homeobox TF | Yes |
| GRHL3 | two hybrid array | 32296183 | Transcription factor | Yes |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 实验分 | 功能类别 | 调控相关？ |
|---------|-------|--------|---------|-----------|
| TLE5 | 0.825 | 0.791 | Corepressor | Yes |
| TLE1 | 0.819 | 0.788 | Corepressor | Yes |
| TLE2 | 0.803 | 0.786 | Corepressor | Yes |
| TLE4 | 0.798 | 0.787 | Corepressor | Yes |
| TLE3 | 0.745 | 0.731 | Corepressor | Yes |
| MESP2 | 0.697 | 0 | Somite TF | Yes |
| TBX6 | 0.615 | 0 | T-box TF | Yes |
| UNCX | 0.508 | 0 | Homeobox TF | Yes |

**评价**: STRING 14 + IntAct 15。PPI 网络核心为 TLE 家族 (TLE1-5) 共抑制因子，IntAct 五条 coIP 实验全部验证。含 HDAC7 (组蛋白去乙酰化酶)、THAP1 (DNA 结合)、PBX4/GRHL3 (转录因子) 和 MED19 (Mediator)。转录调控网络明确且一致。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | PDB 0 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 单一结构域 | 一致 |
| PPI 网络 | STRING + IntAct | TLE 家族 + HDAC/THAP1 | 多源互证 |
| 核定位 | HPA/UniProt/GO | 仅预测级 | 单一来源 |

**互证加分明细**: 无显著额外互证加分。
**总计**: +0

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. TLE/Groucho 转录共抑制因子衔接蛋白，HDAC 招募介导的转录抑制
2. PPI 网络 TLE1-5 五成员全部 coIP 验证，强制可靠
3. IntAct 含 HDAC7 (组蛋白去乙酰化酶)，直接连接染色质修饰
4. 极高新颖性 (PubMed strict=17)，2025 年刚报道肝癌功能
5. 小蛋白 (151 aa)，实验极其友好

**风险/不确定性**:
1. 核定位仅为预测级，需 IF 验证
2. 无 PDB 结构，AF pLDDT 偏低 (59.8)，可能需结合伴侣 (TLE) 才稳定折叠
3. 独立 DNA 结合能力未证实，通过 T-box 因子间接靶向 DNA
4. 研究极少 (17 篇)，功能验证工作量较大

**下一步建议**:
- [ ] IF 实验验证核定位及在不同细胞系中的表达
- [ ] Co-IP/MS 鉴定完整 RIPPLY1 复合体，关注染色质修饰酶
- [ ] 解析 RIPPLY1-TLE 复合体结构 (TLE 已有良好结构基础)
- [ ] 在肝癌模型中验证 RIPPLY1 是否调控 TE 转录

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=RIPPLY1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000147223-RIPPLY1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RIPPLY1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q0D2K3
- STRING: https://string-db.org/network/9606.ENSG00000147223
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q0D2K3

**HPA IF 状态**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。 — HPA 暂无 IF 原图数据。核定位基于 UniProt + GO-CC。


#### PPI 网络
| Partner | Source | Score/Evidence |
|---|---|---|
| TLE5 | STRING | 0.825 |
| TLE1 | STRING | 0.819 |
| TLE2 | STRING | 0.803 |
| TLE4 | STRING | 0.798 |
| TLE3 | STRING | 0.745 |
| TLE2 | IntAct | psi-mi:"MI:0007"(anti tag coim |
| TLE3 | IntAct | psi-mi:"MI:0007"(anti tag coim |
| TLE5 | IntAct | psi-mi:"MI:0007"(anti tag coim |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/RIPPLY1/RIPPLY1-PAE.png]]

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q0D2K3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
