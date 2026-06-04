---
type: protein-evaluation
gene: "LRRC23"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LRRC23 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LRRC23 / LRPB7 |
| 蛋白名称 | Leucine-rich repeat-containing protein 23 |
| 蛋白大小 | 343 aa / 39.8 kDa |
| UniProt ID | Q53EV4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli, Nucleoli rim; UniProt: Cell projection, cilium, flagellum; Cytoplasm, cytoskeleton, |
| 蛋白大小 | 10/10 | ×1 | 10 | 343 aa / 39.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001611, IPR032675, IPR050836; Pfam: PF14580 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.0/180** | |
| **归一化总分** | | | **70.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Nucleoli rim | Approved |
| UniProt | Cell projection, cilium, flagellum; Cytoplasm, cytoskeleton, flagellum axoneme; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- sperm flagellum (GO:0036126)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 18 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LRPB7 |

**关键文献**:
1. LRRC23 truncation impairs radial spoke 3 head assembly and sperm motility underlying male infertility.. *eLife*. PMID: 38091523
2. Proximity labeling of axonemal protein CFAP91 identifies EFCAB5 that regulates sperm motility.. *Nature communications*. PMID: 40931011
3. Network study of nasal transcriptome profiles reveals master regulator genes of asthma.. *The Journal of allergy and clinical immunology*. PMID: 32828590
4. LRRC23 truncation impairs radial spoke 3 head assembly and sperm motility underlying male infertility.. *bioRxiv : the preprint server for biology*. PMID: 36865175
5. Radial spoke proteins regulate otolith formation during early zebrafish development.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 29475374

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.2 |
| 高置信度残基 (pLDDT>90) 占比 | 80.8% |
| 置信残基 (pLDDT 70-90) 占比 | 2.6% |
| 中等置信 (pLDDT 50-70) 占比 | 5.5% |
| 低置信 (pLDDT<50) 占比 | 11.1% |
| 有序区域 (pLDDT>70) 占比 | 83.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.2，有序区 83.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001611, IPR032675, IPR050836; Pfam: PF14580 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TSNAXIP1 | 0.672 | 0.100 | — |
| CCDC113 | 0.651 | 0.000 | — |
| CFAP52 | 0.648 | 0.091 | — |
| LRRC34 | 0.619 | 0.000 | — |
| CFAP161 | 0.588 | 0.000 | — |
| RSPH14 | 0.570 | 0.058 | — |
| CCDC146 | 0.538 | 0.053 | — |
| CFAP45 | 0.535 | 0.045 | — |
| CFAP74 | 0.530 | 0.189 | — |
| DLEC1 | 0.525 | 0.099 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.2 + PDB: 无 | pLDDT=88.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, cilium, flagellum; Cytoplasm, cyt / Nucleoli, Nucleoli rim | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. LRRC23 — Leucine-rich repeat-containing protein 23，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小343 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q53EV4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000010626-LRRC23/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LRRC23
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q53EV4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
