---
type: protein-evaluation
gene: "OASL"
date: 2026-05-28
tags: [protein-scout, evaluation]
status: scored
---

## OASL 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | OASL / 2'-5'-oligoadenylate synthetase-like / p59 / TRIP14 |
| 蛋白大小 | 514 aa / ~59 kDa |
| UniProt ID | Q15646 |
| 评估日期 | 2026-05-28 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4 | /10 | ×3 = 12 | UniProt Nucleus/nucleolus+Cytoplasm; Protein Atlas nucleoplasm+cytosol (Supported); 核质双分布 |
| 📏 蛋白大小 | 10 | /10 | ×2 = 20 | 514 aa，300-800最佳区间 |
| 🆕 研究新颖性 | 5 | /10 | ×3 = 15 | PubMed 380篇；200-500区间 |
| 🏗️ 三维结构 | 10 | /10 | ×3 = 30 | 平均pLDDT极高；96.1%有序；OAS+Ubl双域结构完整 |
| 🧬 调控结构域 | 1 | /10 | ×2 = 2 | OAS域+Ubiquitin-like域；与chromatin/DNA无关 |
| 🔗 PPI | 0/10 | ×3 | **0** | 详见 3.6 PPI 分析 |
| ➕ 互证加分 | +1.0 | max +3 | — | 结构域多库互证+0.5；定位双源互证+0.5 |
| **原始总分** | | | **82.5 / 158** |
| **归一化总分** | | | **52.2 / 100** |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt (Q15646) | Nucleus, nucleolus; Cytoplasm | 注释 |
| Protein Atlas (HPA001474) | Nucleoplasm (Approved), Cytosol (Supported) | Supported |
| GO Cellular Component | Nucleolus, Nucleoplasm, Cytoplasm, Cytosol | IBA/IEA |

**结论**: 核质双分布蛋白。Protein Atlas 在 A-431 和 RT-4 中显示核质+胞质双信号；但在 U2OS 中仅检测到胞质（RNA表达仅2.0 nTPM），提示定位可能与表达水平或细胞类型相关。无明显的核偏好。评分 4。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/OASL/IF_images/A431_HPA001474_1.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/OASL/IF_images/RT4_HPA001474_1.jpg]]

**IF 图像**:

#### 3.2 蛋白大小评估

![[Projects/TEreg-finding/protein-interested/detail/rejected/OASL/OASL-PAE.png]]

**评价**: 514 aa (~59 kDa)。完美落入 300-800 aa 的 sweet spot，适合所有常规生化实验。评分 10。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 | 380 |
| 最早发表年份 | 1999 |
| Chromatin/epigenetics 比例 | 0% |

**主要研究方向**: 抗病毒先天免疫。OASL 是无 2-5A 合成活性的 OAS 家族成员，通过结合 dsRNA 及 RIG-I 增强抗病毒信号。C 端两个 ubiquitin-like 结构域参与蛋白互作。主要研究方向包括抗 HCV、抗 EMCV、IFN 信号通路调控、自身免疫病关联。

**评价**: 中度热门的先天免疫蛋白。研究方向完全聚焦于抗病毒免疫，无 chromatin/epigenetics 研究。评分 5。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 极高（96.1%有序） |
| PDB 实验结构 | — |
| 有序区域 (pLDDT>70) 占比 | 96.1% |
| 高置信度 (pLDDT>90) 占比 | 81.9% |
| 无序区域 (pLDDT<50) 占比 | 1.8% |
| 可用 PDB 条目 | OASL 部分结构已有晶体学数据 |

**评价**: 结构质量近乎完美。81.9% 高置信度，仅 1.8% 无序。OAS domain + 两个 ubiquitin-like domain 均为完整折叠。评分 10。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| Pfam | OAS1_C, ubiquitin (×2) |
| InterPro | NT_2-5OAS_ClassI-CCAase, Ubiquitin-like_dom, Ubiquitin-like_domsf |
| SMART | UBQ |
| CDD | NT_2-5OAS_ClassI-CCAase, Ubl1_OASL, Ubl2_OASL |
| PROSITE | 25A_SYNTH_1/2/3, UBIQUITIN_2 |

**染色质调控潜力分析**: 所有结构域均为 OAS/dsRNA 结合 + ubiquitin-like 蛋白互作结构域。Ubiquitin-like domain 虽然与 ubiquitin 信号通路相关，但并非 chromatin-modifying 的 ubiquitin ligase/deubiquitinase。无 DNA/chromatin 结合域。评分 1。

#### 3.6 PPI :
| Partner | Score | 功能类别 |
|---|---|---|
| ISG15 | 0.999 | Ubiquitin-like antiviral |
| MX1 | 0.958 | Antiviral GTPase |
| HERC5 | 0.956 | Ubiquitin ligase, antiviral |
| RSAD2 | 0.954 | Antiviral (viperin) |
| IFIT1 | 0.949 | RNA binding antiviral |
| DDX58 | 0.940 | RIG-I |
| IFI44 | 0.939 | IFN-induced |
| IRF7 | 0.936 | IFN regulatory TF |
| OAS2 | 0.916 | 2-5A synthetase paralog |
| IFIT3 | 0.902 | RNA binding antiviral |
| STAT1 | 0.886 | IFN signaling TF |
| IFIH1 | 0.857 | MDA5, viral RNA sensor |
| RNASEL | 0.690 | 2-5A activated RNase |

**评价**: 纯抗病毒先天免疫→ +0.5
- ≥2 个独立来源确认定位 (PA + UniProt) → +0.5

**总分**: +1.0 / max +3

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AlphaFold + PDB | 见 3.4 节 | — |
| 结构域 | UniProt / InterPro / Pfam | 见 3.5 节 | — |
| PPI | STRING | 见 3.6 节 | — |
| 定位 | Protein Atlas IF / UniProt / GO | Nucleus | ✅ |

### 4. 总体评价

**推荐等级**: ⭐ (1/5)

**核心优势**: 无——从 chromatin/nuclear biology 角度无吸引力。

**风险/不确定性**: 功能完全定位于先天免疫/抗病毒。虽然 OASL 有核信号且有独特的 ubiquitin-like domain（可能参与核蛋白降解），但整个研究方向与 TEreg/chromatin 不相关。

**结论**: 不推荐作为染色质/转录调控实验室的研究目标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15646
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135114-OASL
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22OASL%22
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15646
- STRING: https://string-db.org/network/9606.ENSP00000257570


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/OASL/OASL-PAE.png]]




