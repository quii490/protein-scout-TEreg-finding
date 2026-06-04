---
type: protein-evaluation
gene: "HMX2"
date: 2026-06-01
tags: [protein-scout, nucleoplasm, evaluation]
status: scored
---

## HMX2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | HMX2 / Homeobox protein HMX2 |
| 蛋白全名 | Homeobox protein HMX2 |
| 蛋白大小 | 273 aa / 29.6 kDa |
| UniProt ID | A2RU54 |

**HPA IF 状态**: HPA IF 暂无数据 (HPA reliability: null, 无可检测定位信号)。核定位基于 UniProt + GO。

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | HPA 无定位数据; UniProt: Nucleus (ECO:0000255); GO: chromatin+nucleus |
| 蛋白大小 | 8/10 | x1 | 8.0 | 273 aa, 29.6 kDa, homeobox 转录因子 |
| 研究新颖性 | 8/10 | x5 | 40.0 | PubMed strict=37, 非常新颖 |
| 三维结构 | 6/10 | x3 | 18.0 | AlphaFold pLDDT=64.6, pct>90=22.0%; 无 PDB |
| 调控结构域 | 7/10 | x2 | 14.0 | Homeobox domain (PF00046); 转录因子; GO chromatin (ISA) |
| PPI 网络 | 4/10 | x3 | 12.0 | IntAct: STAMBPL1/USP38 (coIP), CALB2/LHPP (coIP); STRING: GAL/PAX2 (textmining) |
| **加权总分** | | | **108/180**** | |
| 互证加分 | | | +0.0 | HPA 无定位信号, 无法互证 |
| **归一化总分 (÷1.83)** | | | **59.0/100**** | |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| HPA | 无定位数据 (reliability: null) | 未确认 |
| UniProt | Nucleus (ECO:0000255) | 预测 |
| GO-CC | chromatin (ISA), nucleus (IBA) | 预测 |

**HPA IF 状态**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。 -- HPA 无可用定位数据。核定位仅基于 UniProt 预测和 GO 注释，需内源 IF 验证。

**结论**: 低置信度核蛋白候选。Homeobox 家族蛋白通常定位于核，但 HMX2 缺少直接实验定位证据。

#### 3.2 蛋白大小评估
273 aa, 29.6 kDa。Homeobox 转录因子，大小适中，适合重组表达。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict (Title/Abstract) | 37 |
| PubMed broad | 72 |
| 新颖性级别 | 非常新颖 |

PubMed 共 37 篇严格文献。研究较少，主要集中在内耳发育、肾脏 intercalated cell 分化方向。niche 空间充足。

**关键文献**:
1. Parvez RK et al. (2025). "Dmrt2 and Hmx2 direct intercalated cell diversity in the mammalian kidney through antagonistic and supporting regulatory processes." *Proc Natl Acad Sci U S A*. PMID: 40354537
2. Feng Y et al. (2026). "Hmx2 and Dmrt2 Coordinate the Differentiation of Intercalated Cell Subtypes in Kidney." *J Am Soc Nephrol*. PMID: 41051882
3. Wang W & Lufkin T (2005). "Hmx homeobox gene function in inner ear and nervous system cell-type specification and development." *Exp Cell Res*. PMID: 15925593
4. Nagel S et al. (2020). "Aberrant expression of NKL homeobox genes HMX2 and HMX3 interferes with cell differentiation in acute myeloid leukemia." *PLoS One*. PMID: 33048949
5. Wang W et al. (2001). "Hmx2 homeobox gene control of murine vestibular morphogenesis." *Development*. PMID: 11748138

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold | AF-A2RU54-F1 v6 |
| 平均 pLDDT | 64.6 |
| pLDDT >90 | 22.0% |
| pLDDT 70-90 | 8.1% |
| pLDDT 50-70 | 41.0% |
| pLDDT <50 | 28.9% |
| PDB | 无 |

**AlphaFold PAE**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HMX2/HMX2-PAE.png]]

较低 pLDDT 均值 (64.6)，仅 22% 区域 >90 置信度。Homeobox domain 区域预测置信度较高，其余区域存在显著无序。

#### 3.5 结构域分析
| 来源 | 结构域 | 备注 |
|---|---|---|
| InterPro | IPR001356 (Homeobox), IPR020479 (Homeobox metazoa), IPR051300, IPR017970 (Homeobox conserved site), IPR009057 (Homeobox-like superfamily) | 经典 homeobox 转录因子 |
| Pfam | PF00046 (Homeobox) | DNA-binding homeodomain |

Homeobox 转录因子，具有经典 DNA-binding homeodomain。GO-CC 注释为 chromatin (ISA:NTNU_SB)，支持染色质结合功能。

#### 3.6 PPI 网络（三源综合）

**实验验证互作 (IntAct)**:
| Partner | 方法 | PMID | 功能类别 |
|---|---|---|---|
| STAMBPL1 | anti tag coIP | 19615732 | Deubiquitination |
| USP38 | anti tag coIP | 19615732 | Deubiquitination |
| CALB2 | anti tag coIP | 33961781 | Calcium binding |
| LHPP | anti tag coIP | 33961781 | Phosphatase |

**STRING 预测互作 (combined score >0.4)**:
| Partner | Score | 证据类型 |
|---|---|---|
| GAL | 0.687 | textmining |
| PAX2 | 0.624 | experimental=0.060, textmining=0.616 |
| BUB3 | 0.566 | textmining |

**UniProt 记录互作**: 无

STAMBPL1/USP38 的 coIP 互作来自同一项研究 (PMID:19615732)，CALB2/LHPP 来自 BioPlex 3.0。PPI 网络较稀疏。

#### 3.7 多库互证
| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 定位 | HPA / UniProt / GO | 无信号 / Nucleus / chromatin+nucleus | HPA 为空, UniProt/GO 一致但均为预测 |
| PPI | STRING / IntAct | 独立互作, 无重叠 | 无多源互证 |
| 结构 | AlphaFold only | pLDDT=64.6 | 无 PDB 互证 |

**互证加分明细**: 无
**总计**: +0 / max +3

### 4. 总体评价

**推荐等级**: 2星 (59.0/100)

HMX2 是 Homeobox 转录因子，PubMed 仅 37 篇，非常新颖。但 HPA 无可用定位数据，核定位置信度偏低。结构预测中等。如能通过内源 IF 确认核定位，可提升评分。

**核心优势**:
1. PubMed=37，非常新颖
2. 具 homeobox DNA-binding domain，明确转录因子
3. 大小适中 (273 aa)

**风险/不确定性**:
1. HPA 无定位数据，核定位需验证
2. AlphaFold 结构置信度偏低 (pLDDT=64.6)
3. PPI 网络稀疏，缺少功能验证互作

**下一步建议**:
- 内源 IF / 核-质分离 WB 验证核定位
- Co-IP/MS 鉴定互作伙伴
- 功能获得/缺失实验（肾脏或内耳方向）

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A2RU54
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A2RU54
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22HMX2%22%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/ENSG00000188816-HMX2

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HMX2/HMX2-PAE.png]]
