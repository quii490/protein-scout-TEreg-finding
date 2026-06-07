---
type: protein-evaluation
gene: "XRN2"
date: 2026-05-28
tags: [protein-scout, nuclear-protein, evaluation, scored]
status: scored
_date: 2026-05-29
_notes: "PubMed=199 (≥100, 无基线调整); HPA Enhanced→核=10; 新降级8→7; PDB查无人类结构(仅酵母Rat1同源)"
---

## XRN2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | XRN2 / 5'-3' exoribonuclease 2 / Rat1 homolog |
| 蛋白大小 | 950 aa / ~108 kDa |
| UniProt ID | Q9H0D6 |
| 评估日期 | 2026-05-28 () / 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 得分 | 关键证据摘要 |
|---|---|---|---|---|---|
| 🔴 核定位特异性 | 10/10 | ×3 | 30.0 | 10 | HPA Enhanced (最高等级), 核仁+核质; 双重抗体三细胞系验证 |
| 📏 蛋白大小 | 8/10 | ×2 | 16.0 | 8 | 950 aa, 略超800上限 |
| 🆕 研究新颖性 | 7/10 | ×3 | 21.0 | 8 | PubMed=199 (≥100, 无基线); 199篇偏多但chromatin方向极少 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21.0 | 7 | pLDDT 76.5; 71.5%有序; PDB无人类结构(仅酵母Rat1); ≥100无基线 |
| 🧬 调控结构域 | 5/10 | ×2 | 10.0 | 5 | XRN exonuclease + CCHC ZnF; ≥100无域基线提升 |
| 🔗 PPI | 0/10 | ×3 | **0** | 详见 3.6 PPI 分析 |
| **原始总分** | | | **109.0/158** | 112.0 | |
| **归一化总分** | | | **69.0/100** | 70.9 | **Δ = -1.9** |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt (Q9H0D6) | Nucleus, nucleolus | 注释 |
| GO Cellular Component | Nucleus, Nucleolus, Nucleoplasm | IBA/IDA |
| Protein Atlas (HPA047118, HPA050485) | Nucleoli (Enhanced), Nucleoplasm (Enhanced) | Enhanced - 最高等级 |

**结论**: 严格的核仁+核质蛋白。Protein Atlas Enhanced 等级（最高可信度），HEK293/MCF-7/U2OS 三种细胞系双重抗体验证一致。评分 10。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/XRN2/IF_images/U2OS_HPA047118.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/XRN2/IF_images/MCF7_HPA047118.jpg]]

**IF 图像**:

#### 3.2 蛋白大小评估
**评价**: 950 aa (~108 kDa)。略高于 800 aa 理想上限，但仍在 800-1200 aa 的可操作范围。对于生化实验（尤其是 exonuclease 活性测定）有一定难度，但表达和纯化是可行的（文献中有大量 XRN2 体外实验报道）。评分 8。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 (gene+protein filter) | 150 |
| PubMed 总数 (gene only) | 199 |
| 最早发表年份 | 1999 |
| Chromatin/epigenetics 比例 | <5% |

**主要研究方向**:
- 转录终止：XRN2 通过 torpedo 模型在 polyA 位点后降解 RNA，促进 Pol II 终止
- R-loop 分辨率：XRN2 结合 G-rich pause site 形成的 R-loops
- RNA 代谢：5'-3' exoribonuclease 活性，参与 rRNA processing
- 少数研究涉及 XRN2 在 DNA 损伤应答和核糖体应激中的作用

**评价**: XRN2 有近 200 篇文献，但几乎全部聚焦于 RNA processing。与 chromatin/DNA 直接相关的研究极少，主要是在转录终止这个交叉点上。作为研究较深入的蛋白，新颖性在 chromatin 方向仍然较高。评分 8。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 76.5 |
| PDB 实验结构 | — |
| 有序区域 (pLDDT>70) 占比 | 71.5% |
| 高置信度 (pLDDT>90) 区域 | 502 aa (52.8%) |
| 无序区域 (pLDDT<50) 占比 | 20.5% (残基408-508, 911-950) |
| 可用 PDB 条目 | 部分细菌/酵母 Rat1 同源物结构 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/XRN2/XRN2-PAE.png]]

**评价**: 结构质量良好。52.8% 高置信度折叠，平均 pLDDT 76.5。XRN_N 和 XRN_M 折叠域分明，存在明确的域间结构。两个 IDR 区域（408-508, 911-950）可能为调节区。整体结构适合进行结构-功能研究。评分 7。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| Pfam | XRN_N (PF03159), XRN_M (PF18363) |
| InterPro | Xrn1_N (IPR027073), Xrn1_helical (IPR041412), Xrn2/3/4 (IPR047763), 5_3_exoribonuclease (IPR017151) |
| CDD | PIN_XRN1-2-like |
| Gene3D | — |
| GeneCards | Region:Disordered(408-508); Region:Disordered(911-950) |
| UniProt | CCHC-type zinc finger (262-278), Disordered (408-508, 911-950) |

**染色质调控潜力分析**: XRN 结构域家族是经典的外切核酸酶结构域，非直接 chromatin/DNA 结合域。但 UniProt GO 标注了 "transcription termination site sequence-specific DNA binding"，表明 XRN2 在转录终止位点有序列特异性 DNA 结合活性。CCHC 锌指可能参与核酸结合。XRN2 在转录终止中的角色使其与 Pol II 染色质占位有间接关联。评分 5（非chromatin结构域但有 transcription termination DNA binding 活性）。

#### 3.6 PPI :
| Partner | Score | 功能类别 | 与调控相关？ |
|---|---|---|---|
| MTREX | 0.995 | Nuclear exosome cofactor | — (RNA processing) |
| CPSF3 | 0.989 | Cleavage/polyadenylation factor | — (RNA processing) |
| EXOSC10 | 0.818 | Exosome component | — (RNA processing) |
| XRN1 | 0.654 | 5'-3' exonuclease (cytoplasmic paralog) | — (RNA processing) |
| DCP2 | 0.578 | mRNA decapping enzyme | — (RNA processing) |
| DICER1 | 0.562 | miRNA processing | — (RNA processing) |
| SETX | 0.466 | Senataxin, transcription termination | ✓ (转录终止) |
| UPF1 | 0.412 | Nonsense-mediated decay | — (RNA processing) |
| UPF2 | 0.582 | NMD factor | — (RNA processing) |
| SKIV2L | 0.547 | RNA helicase | — (RNA processing) |
| FBF1 | 0.447 | Fas binding factor 1 | — |

**调控相关比例**: 1/11 (9.1%)

**humanPPI** (prodata.swmed.edu): 证书错误不可访问。

**评价**: PPI ，反映了 XRN2 的核心生物学角色。评分 4。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AlphaFold pLDDT 76.5 + 同源物PDB结构存在 | AlphaFold 预测良好，同源物有实验结构 | 部分互证 |
| 结构域 | UniProt / Pfam / InterPro / CDD | 四库一致XRN exonuclease域 | ✓ 一致 |
| PPI | STRING (only) + STRING 数据 | 仅单源 | 无互证 |
| 定位 | Protein Atlas (Enhanced) / UniProt / GO | 三源一致核仁+核质 | ✓ 一致 |

**互证加分明细**:
- ≥3 个独立来源检出同一结构域 (XRN家族, 4/4库) → +0.5
- ≥2 个独立来源一致确认核定位 (PA Enhanced + UniProt + GO) → +0.5

**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. **严格的核仁定位**: Protein Atlas Enhanced 最高可信度，双重抗体三细胞系验证
2. **结构质量好**: 71.5% 有序，pLDDT 76.5，明确的域结构
3. **转录终止功能**: 与 Pol II 染色质动态直接相关，存在 R-loop 调控潜力
4. **成熟的实验工具**: 已有抗体、体外实验体系、knock-down 表型

**风险/不确定性**:
1. **研究较多** (199篇): 但 chromatin 方向极少，需要找到差异化的切入角度
2. **PPI : 全长表达和纯化有一定挑战
4. **功能定位于RNA而非chromatin**: 与 TEreg/chromatin 的核心关注点距离较远

**下一步建议**:
- [ ] 探索 XRN2 在特定基因组位点（如 TE 富集区域）的 R-loop 调控角色
- [ ] ChIP-seq 分析 XRN2 是否存在非转录终止位点的染色质结合
- [ ] 与 cohesin/CTCF 等染色质架构蛋白的关系

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H0D6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000088930-XRN2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22XRN2%22
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H0D6
- STRING: https://string-db.org/network/9606.ENSP00000366396

![[Projects/TEreg-finding/protein-interested/detail/rejected/XRN2/XRN2-PAE.png]]


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/XRN2/XRN2-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H0D6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR027073;IPR041412;IPR004859;IPR017151; |
| Pfam | PF17846;PF03159; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000088930-XRN2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CDKN2AIP | Intact, Biogrid | true |
| CDKN2AIPNL | Intact, Biogrid | true |
| CRY2 | Intact, Biogrid | true |
| DISC1 | Intact, Biogrid | true |
| TARDBP | Intact, Biogrid | true |
| ANLN | Biogrid | false |
| APP | Intact | false |
| AR | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
