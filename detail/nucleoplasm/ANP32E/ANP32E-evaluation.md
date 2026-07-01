---
type: protein-evaluation
gene: "ANP32E"
date: 2026-06-01
tags: [protein-scout, nucleoplasm, evaluation]
status: scored
---

## ANP32E 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | ANP32E |
| 蛋白全名 | Acidic leucine-rich nuclear phosphoprotein 32 family member E |
| 蛋白大小 | 268 aa / ~30 kDa |
| UniProt ID | Q9BTT0 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | ANP32 nuclear phosphoprotein; SWR1 complex (H2A.Z deposition); GO nucleus IDA:LIFEdb; UniProt Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8.0 | 268 aa |
| 研究新颖性 | 6/10 | ×5 | 30.0 | PubMed strict=52 (≤60) |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT 76.4; 2 PDB (X-ray 3.0 Å) |
| 调控结构域 | 7/10 | ×2 | 14.0 | Leucine-rich repeat; H2A.Z histone chaperone; SWR1/SRCAP complex |
| PPI 网络 | 8/10 | ×3 | 24.0 | H2AZ1 (0.996), EP400 (0.992), KAT5 (0.984) — chromatin remodeling |
| **加权总分** | | | **129/180********** | |
| 互证加分 | | | +2.0 | SWR1 chromatin complex + H2A.Z chaperone + ANP32 nuclear family |
| **归一化总分 (÷1.83)** | | | **70.5/100********** | |

PubMed strict: 52

### 3. 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Cytoplasm (ECO:0000250); Nucleus (ECO:0000250) | Sequence similarity |
| GO-CC | nucleus IDA:LIFEdb; Swr1 complex IDA:UniProtKB; synaptic vesicle membrane IEA | Direct assay (nucleus) |
| Protein family | ANP32 — Acidic Nuclear Phosphoprotein 32 | Naming |
| HPA IF | Nucleoplasm + Nuclear membrane (main) | HPA localization available |

**HPA IF 数据**: HPA subcellular localization available. Full red_green IF image acquired (776 KB). Antibody HPA041206.

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ANP32E/IF_images/ANP32E_IF_red_green.jpg]]

**HPA IF 状态**: IF full acquired — HPA IF 原图 (red_green, 776 KB) 已成功获取并嵌入。HPA 数据库包含 24 张 red_green IF 图像。

ANP32E 是 ANP32 (acidic nuclear phosphoprotein) 家族成员。作为 H2A.Z 组蛋白伴侣和 SWR1/SRCAP 染色质重塑复合体组分，其核定位是功能必需的。GO nucleus IDA:LIFEdb 为荧光显微镜实验确认。

### 4. 研究现状

| 指标 | 数值 |
|---|---|
| PubMed strict | 52 |
| PubMed broad | 85 |

**关键文献**: ANP32E 是 H2A.Z 特异的组蛋白伴侣，催化 H2A.Z-H2B 在染色质上的沉积和移除，调控转录、DNA repair、染色体分离。与 EP400 (SWR1/SRCAP ATPase) 和 KAT5 (Tip60 乙酰转移酶) 形成染色质重塑复合体。文献涵盖 H2A.Z 生物学、癌症表观遗传学和胚胎发育。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| EP400 | STRING | 992 |
| KAT5 | STRING | 984 |
| TRRAP | STRING | 953 |
| BRD8 | STRING | 950 |
| RUVBL1 | STRING | 949 |
| HIST1H2BJ | STRING | 947 |
| ING3 | STRING | 941 |
| RUVBL2 | STRING | 939 |


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/ANP32E

### PubMed

**Count: 138**

| PMID | Title |
|---|---|
| 42333064 | In silico analysis suggests ELL2 as a survival-associated cross-tissue biomarker in gastric cancer. |
| 42185655 | Single-cell eQTL-based Mendelian randomization identifies immune cell subtype-specific regulators of epigenetic aging and prioritizes candidate therap |
| 42075256 | Historical Pandemic and Contemporary Influenza A Viruses Reveal PB2 M631L as a Convergent Adaptation to Human ANP32. |
| 41989318 | From Initiation to Elongation: eIF3 as a Dual-Phase Guardian of Mitochondrial Integrity and Protein Homeostasis in Skeletal Muscle. |
| 41980942 | ANP32E drives lung adenocarcinoma progression via GSK3β-mediated glycolytic reprogramming. |


