---
type: protein-evaluation
gene: "NRBF2"
date: 2026-06-04
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NRBF2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NRBF2 / COPR |
| 蛋白名称 | Nuclear receptor-binding factor 2 |
| 蛋白大小 | 287 aa / 32.4 kDa |
| UniProt ID | Q96F24 |
| 评估日期 | 2026-06-04 |

**功能简介** (UniProt): May modulate transcriptional activation by target nuclear receptors. Can act as transcriptional activator (in vitro)

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Nucleus; Cytoplasm; Cytoplasmic vesicle; Cytoplasmic vesicle |
| 蛋白大小 | 10/10 | ×1 | 10 | 287 aa / 32.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=33 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=72.9; PDB: 4ZEY |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039679, IPR015056, IPR033393; Pfam: PF08961, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.0/180** | |
| **归一化总分** | | | **70.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Nucleus; Cytoplasm; Cytoplasmic vesicle; Cytoplasmic vesicle, autophagosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- autophagosome (GO:0005776)
- cytoplasm (GO:0005737)
- cytoplasmic vesicle (GO:0031410)
- nucleoplasm (GO:0005654)
- phosphatidylinositol 3-kinase complex, class III (GO:0035032)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 33 |
| PubMed broad count | 45 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: COPR |

**关键文献**:
1. How autophagy controls the intestinal epithelial barrier.. *Autophagy*. PMID: 33906557
2. PI3KC3 complex subunit NRBF2 is required for apoptotic cell clearance to restrict intestinal inflammation.. *Autophagy*. PMID: 32160108
3. Autophagy in colitis-associated colon cancer: exploring its potential role in reducing initiation and preventing IBD-Related CAC development.. *Autophagy*. PMID: 37723664
4. The potent BECN2-ATG14 coiled-coil interaction is selectively critical for endolysosomal degradation of GPRASP1/GASP1-associated GPCRs.. *Autophagy*. PMID: 37409929
5. Autophagy protein NRBF2 attenuates endoplasmic reticulum stress-associated neuroinflammation and oxidative stress via promoting autophagosome maturation by interacting with Rab7 after SAH.. *Journal of neuroinflammation*. PMID: 34530854

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.9 |
| 高置信度残基 (pLDDT>90) 占比 | 41.5% |
| 置信残基 (pLDDT 70-90) 占比 | 10.5% |
| 中等置信 (pLDDT 50-70) 占比 | 25.4% |
| 低置信 (pLDDT<50) 占比 | 22.6% |
| 有序区域 (pLDDT>70) 占比 | 52.0% |
| 可用 PDB 条目 | 4ZEY |

**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=72.9，有序区 52.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039679, IPR015056, IPR033393; Pfam: PF08961, PF17169 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BECN1 | 0.999 | 0.994 | — |
| PIK3C3 | 0.999 | 0.994 | — |
| ULK1 | 0.999 | 0.994 | — |
| ATG14 | 0.999 | 0.994 | — |
| RB1CC1 | 0.999 | 0.994 | — |
| PIK3R4 | 0.999 | 0.994 | — |
| ATG101 | 0.962 | 0.000 | — |
| UVRAG | 0.943 | 0.095 | — |
| ULK2 | 0.942 | 0.000 | — |
| BECN2 | 0.934 | 0.051 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%，尚无实验验证互作。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.9 + PDB: 4ZEY | pLDDT=72.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasmic vesicle; Cytoplasm / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. NRBF2 — Nuclear receptor-binding factor 2，非常新颖，仅有少数基础研究。
2. 蛋白大小287 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 33 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96F24
- Protein Atlas: https://www.proteinatlas.org/ENSG00000148572-NRBF2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NRBF2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96F24
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live via harvest pipeline; evaluated 2026-06-04

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000148572-NRBF2/subcellular

![](https://images.proteinatlas.org/59477/1018_F5_1_red_green.jpg)
![](https://images.proteinatlas.org/59477/1018_F5_2_red_green.jpg)
![](https://images.proteinatlas.org/59477/1218_F5_1_red_green.jpg)
![](https://images.proteinatlas.org/59477/1218_F5_2_red_green.jpg)
![](https://images.proteinatlas.org/59477/1259_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/59477/1259_F7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
