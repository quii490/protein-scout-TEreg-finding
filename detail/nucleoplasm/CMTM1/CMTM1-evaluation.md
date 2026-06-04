---
type: protein-evaluation
gene: "CMTM1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CMTM1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CMTM1 / CKLFSF1 |
| 蛋白名称 | CKLF-like MARVEL transmembrane domain-containing protein 1 |
| 蛋白大小 | 169 aa / 18.6 kDa |
| UniProt ID | Q8IZ96 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: Membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 169 aa / 18.6 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=25 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008253, IPR050578 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **105.5/180** | |
| **归一化总分** | | | **58.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- extracellular space (GO:0005615)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 25 |
| PubMed broad count | 31 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CKLFSF1 |

**关键文献**:
1. Expression and clinical significance of CMTM1 in hepatocellular carcinoma.. *Open medicine (Warsaw, Poland)*. PMID: 33585698
2. Systemic AAV8-Mediated Gene Therapy Drives Whole-Body Correction of Myotubular Myopathy in Dogs.. *Molecular therapy : the journal of the American Society of Gene Therapy*. PMID: 28237839
3. A novel protein CMTM1-v5 specifically induced human lymphoma cells apoptosis in vitro and in vivo.. *Experimental cell research*. PMID: 31542285
4. rAAV-related therapy fully rescues myonuclear and myofilament function in X-linked myotubular myopathy.. *Acta neuropathologica communications*. PMID: 33076971
5. Current Opinions on the Relationship Between CMTM Family and Hepatocellular Carcinoma.. *Journal of hepatocellular carcinoma*. PMID: 37649636

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.7 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 46.7% |
| 中等置信 (pLDDT 50-70) 占比 | 45.6% |
| 低置信 (pLDDT<50) 占比 | 7.7% |
| 有序区域 (pLDDT>70) 占比 | 46.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=66.7），有序残基占 46.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008253, IPR050578 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CMTM3 | 0.975 | 0.000 | — |
| CMTM4 | 0.968 | 0.000 | — |
| CMTM7 | 0.946 | 0.000 | — |
| CMTM5 | 0.849 | 0.000 | — |
| CMTM6 | 0.817 | 0.000 | — |
| CMTM8 | 0.754 | 0.000 | — |
| MTM1 | 0.577 | 0.000 | — |
| TSPAN1 | 0.570 | 0.000 | — |
| CMTM2 | 0.536 | 0.000 | — |
| CCL17 | 0.509 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=66.7 + PDB: 无 | pLDDT=66.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CMTM1 — CKLF-like MARVEL transmembrane domain-containing protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小169 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 25 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=66.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IZ96
- Protein Atlas: https://www.proteinatlas.org/ENSG00000089505-CMTM1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CMTM1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IZ96
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
