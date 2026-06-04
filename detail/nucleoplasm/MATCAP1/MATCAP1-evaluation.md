---
type: protein-evaluation
gene: "MATCAP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MATCAP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MATCAP1 / KIAA0895L, MATCAP |
| 蛋白名称 | Microtubule-associated tyrosine carboxypeptidase 1 |
| 蛋白大小 | 471 aa / 53.4 kDa |
| UniProt ID | Q68EN5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Vesicles; UniProt: Cytoplasm, cytoskeleton |
| 蛋白大小 | 10/10 | ×1 | 10 | 471 aa / 53.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=76.6; PDB: 7Z5G, 7Z5H, 7Z6S |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR012548; Pfam: PF08014 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.5/180** | |
| **归一化总分** | | | **69.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles | Approved |
| UniProt | Cytoplasm, cytoskeleton | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- microtubule (GO:0005874)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 2 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0895L, MATCAP |

**关键文献**:
1. MATCAP1 preferentially binds an expanded tubulin conformation to generate detyrosinated and ΔC2 α-tubulin.. *bioRxiv : the preprint server for biology*. PMID: 40894690
2. MATCAP1 preferentially binds an expanded tubulin conformation to generate detyrosinated and ΔC2 α-tubulin.. *The EMBO journal*. PMID: 41974940

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.6 |
| 高置信度残基 (pLDDT>90) 占比 | 62.4% |
| 置信残基 (pLDDT 70-90) 占比 | 7.9% |
| 中等置信 (pLDDT 50-70) 占比 | 2.5% |
| 低置信 (pLDDT<50) 占比 | 27.2% |
| 有序区域 (pLDDT>70) 占比 | 70.3% |
| 可用 PDB 条目 | 7Z5G, 7Z5H, 7Z6S |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（7Z5G, 7Z5H, 7Z6S）+ AlphaFold高质量预测（pLDDT=76.6），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012548; Pfam: PF08014 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ZBTB8B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ENST00000290881 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 2
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.6 + PDB: 7Z5G, 7Z5H, 7Z6S | pLDDT=76.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton / Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 0 + 2 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MATCAP1 — Microtubule-associated tyrosine carboxypeptidase 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小471 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q68EN5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000196123-MATCAP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MATCAP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q68EN5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
