---
type: protein-evaluation
gene: "PXMP4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PXMP4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PXMP4 / PMP24 |
| 蛋白名称 | Peroxisomal membrane protein 4 |
| 蛋白大小 | 212 aa / 24.3 kDa |
| UniProt ID | Q9Y6I8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Peroxisomes; 额外: Nucleoli fibrillar center; UniProt: Peroxisome membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 212 aa / 24.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=91.8; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR019531; Pfam: PF02466 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Peroxisomes; 额外: Nucleoli fibrillar center | Approved |
| UniProt | Peroxisome membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- peroxisomal membrane (GO:0005778)
- peroxisome (GO:0005777)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 22 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PMP24 |

**关键文献**:
1. High Expression of PXMP4 in Hepatocellular Carcinoma Tissues.. *Asian Pacific journal of cancer prevention : APJCP*. PMID: 38415547
2. HSD17B4, ACAA1, and PXMP4 in Peroxisome Pathway Are Down-Regulated and Have Clinical Significance in Non-small Cell Lung Cancer.. *Frontiers in genetics*. PMID: 32265992
3. PXMP4 promotes gastric cancer cell epithelial-mesenchymal transition via the PI3K/AKT signaling pathway.. *Molecular biology reports*. PMID: 38401002
4. Mice with a deficiency in Peroxisomal Membrane Protein 4 (PXMP4) display mild changes in hepatic lipid metabolism.. *Scientific reports*. PMID: 35169201
5. Identification of four methylation-driven genes as candidate biomarkers for monitoring single-walled carbon nanotube-induced malignant transformation of the lung.. *Toxicology and applied pharmacology*. PMID: 33387576

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.8 |
| 高置信度残基 (pLDDT>90) 占比 | 78.3% |
| 置信残基 (pLDDT 70-90) 占比 | 18.4% |
| 中等置信 (pLDDT 50-70) 占比 | 2.4% |
| 低置信 (pLDDT<50) 占比 | 0.9% |
| 有序区域 (pLDDT>70) 占比 | 96.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=91.8，有序区 96.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019531; Pfam: PF02466 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PEX19 | 0.899 | 0.292 | — |
| PEX11B | 0.815 | 0.000 | — |
| PXMP2 | 0.780 | 0.000 | — |
| SLC25A17 | 0.756 | 0.000 | — |
| PEX16 | 0.751 | 0.000 | — |
| ABCD3 | 0.717 | 0.000 | — |
| PEX13 | 0.716 | 0.000 | — |
| ABCD1 | 0.702 | 0.000 | — |
| ABCD2 | 0.702 | 0.000 | — |
| PEX12 | 0.695 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NS3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33845483|pmc:PPR177217| |
| PGAM2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.8 + PDB: 无 | pLDDT=91.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Peroxisome membrane / Peroxisomes; 额外: Nucleoli fibrillar center | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PXMP4 — Peroxisomal membrane protein 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小212 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y6I8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000101417-PXMP4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PXMP4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y6I8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
