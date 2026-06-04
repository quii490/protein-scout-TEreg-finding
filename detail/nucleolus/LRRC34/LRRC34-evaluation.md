---
type: protein-evaluation
gene: "LRRC34"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LRRC34 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LRRC34 |
| 蛋白名称 | Leucine-rich repeat-containing protein 34 |
| 蛋白大小 | 464 aa / 51.3 kDa |
| UniProt ID | Q8IZ02 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Microtubules; 额外: Cytokinetic bridge, Mitotic spindle, Prima; UniProt: Nucleus; Nucleus, nucleolus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 464 aa / 51.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.9; PDB: 8J07 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001611, IPR052201, IPR032675; Pfam: PF13516 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **135.5/180** | |
| **归一化总分** | | | **75.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Microtubules; 额外: Cytokinetic bridge, Mitotic spindle, Primary cilium, Basal body | Approved |
| UniProt | Nucleus; Nucleus, nucleolus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleolus (GO:0005730)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 21 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. LRRC23 truncation impairs radial spoke 3 head assembly and sperm motility underlying male infertility.. *eLife*. PMID: 38091523
2. Lrrc34, a novel nucleolar protein, interacts with npm1 and ncl and has an impact on pluripotent stem cells.. *Stem cells and development*. PMID: 24991885
3. Variants in LRRC34 reveal distinct mechanisms for predisposition to papillary thyroid carcinoma.. *Journal of medical genetics*. PMID: 32051256
4. Lrrc34 Is Highly Expressed in SSCs and Is Necessary for SSC Expansion In Vitro.. *Chinese medical sciences journal = Chung-kuo i hsueh k'o hsueh tsa chih*. PMID: 32299535
5. Variability in newborn telomere length is explained by inheritance and intrauterine environment.. *BMC medicine*. PMID: 35073935

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.9 |
| 高置信度残基 (pLDDT>90) 占比 | 75.6% |
| 置信残基 (pLDDT 70-90) 占比 | 7.3% |
| 中等置信 (pLDDT 50-70) 占比 | 3.0% |
| 低置信 (pLDDT<50) 占比 | 14.0% |
| 有序区域 (pLDDT>70) 占比 | 82.9% |
| 可用 PDB 条目 | 8J07 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.9，有序区 82.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001611, IPR052201, IPR032675; Pfam: PF13516 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LILRB3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ENST00000446859 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 2
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.9 + PDB: 8J07 | pLDDT=85.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleolus; Cytoplasm / Microtubules; 额外: Cytokinetic bridge, Mitotic spin | 一致 |
| PPI | STRING + IntAct | 0 + 2 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. LRRC34 — Leucine-rich repeat-containing protein 34，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小464 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IZ02
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171757-LRRC34/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LRRC34
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IZ02
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
